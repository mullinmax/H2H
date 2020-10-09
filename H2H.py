import json 

class H2H():

    def __init__(self, lang_spec_path):
        self.load_lang_spec(lang_spec_path)


    def load_lang_spec(self, path):
        with open(path) as json_file:
            self.lang_spec = json.load(json_file)

    def lang_spec_to_md(self, output_path):
        f = open(output_path, 'w')
        output = '''language version: *{version}*

symbol | indent | description      | C code
-------|--------|------------------|---------------------
'''.format(version = self.lang_spec['version'])
        
        esc = lambda t : '`' + t.replace("|", "\|").replace("\n", "\\n") + '`'
        md_cols = lambda t : '|'.join(
            [
                ' ' + esc(t['s']).ljust(6),
                ' ' + esc(t['i']).ljust(7),
                ' ' + t['d'].ljust(17),
                ' ' + esc(t['c']).ljust(20)
            ]
        )
        output += '\n'.join([md_cols(t) for t in self.lang_spec['tokens']])

        f = open(output_path, 'w')
        f.write(output)
        return

    # Build C code
    def H2H_to_C(self, H2H_code, ind = 1):
        symbols = {}
        for t in self.lang_spec['tokens']:
            symbols[t['s']] = t['c']
        print(symbols)
        return self.lang_spec["main-template"].replace('$', self.__H2H_to_C(H2H_code, '', ind, symbols))

    def __H2H_to_C(self, H2H_code, C, ind, symbols):
        if len(H2H_code) == 0:
            return C
        if H2H_code[0] in symbols:
            if '$' in C:
                C = C.replace('$', symbols[H2H_code[0]], 1)
            else:
                C += '    '*ind + symbols[H2H_code[0]]
            return self.__H2H_to_C(H2H_code[1:], C, ind, symbols)
        else:
            return self.__H2H_to_C(H2H_code[1:], C, ind, symbols)



    def compile(self, input_path, output_path):
        H2H_code = read(input_path)
        H2H_to_C(H2H_code)
        write(output_path)
        return code

if __name__ == "__main__":
    compiler = H2H('lang_spec.json')
    print(compiler.H2H_to_C('?1\n"1'))