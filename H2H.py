#!/bin/python

import os

# read language specification
f = open('lang_spec.md')
f.readline()
f.readline()
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
    lang[spec[0]]['C'] = spec[2].replace('\\n', '\n')

# Read source code
f = open('test.H2H')
code = ''.join(f.readlines())
f.close()

# Build C code
C = lang['^']['C'] + '\n'
indent = lang['^']['indent']
for char in code:
    if char in lang:
        C += '\t'*indent + lang[char]['C'] + '\n'
        indent += lang[char]['indent']
C += lang['$']['C']

# Write C code
f = open('H2H.c', 'w')
f.write(C)
f.close()

# Compile C code
os.system('g++ H2H.c')