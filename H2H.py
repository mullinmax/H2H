#!/bin/python

import os

# read language specification
f = open('lang_spec.md')
f.readline() # Ignore version 
f.readline() # Ignore blank spacer line
f.readline() # Ignore table header
f.readline() # Ignore table format line
lang_spec = []
for line in f.readlines():
    row = []
    for cell in line.split('|'):
        row.append(cell.strip()[1:-1])
    lang_spec.append(row)
f.close()

# Build language
lang = {}
for spec in lang_spec:
    lang[spec[0]] = {}
    if spec[1] == '+':
        lang[spec[0]]['indent'] = 1
    elif spec[1] == '-':
        lang[spec[0]]['indent'] = -1
    else:
        lang[spec[0]]['indent'] = 0
    lang[spec[0]]['C'] = spec[3].replace('\\n', '\n')

# Read source code
f = open('test.H2H')
source_code = ''.join(f.readlines())
f.close()

# Build C code
def build_C_code(src, ind):
    if len(src) == 0:
        return ''
    if src[0] in lang:
        code = '$'
        while '$' in code:
            code = code.replace('$', lang[src[0]]['C'], 1)
            ind += lang[src[0]]['indent']
            src = src[1:]
        return '    '*indent + code + '\n' + build_C_code(src, ind)
    else:
        return build_C_code(src[1:], ind)
        

C = lang['BOF']['C'] + '\n'
indent = lang['BOF']['indent']
C += build_C_code(source_code, indent)
C += lang['EOF']['C']

# Write C code
f = open('H2H.c', 'w')
f.write(C)
f.close()

# Compile C code
os.system('g++ -Wall -O3 H2H.c')
