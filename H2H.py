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

    def tokenize(self, str):
        return tokens

    def H2H_to_C(self, H2H_code):
        tokens = tokenize(H2H_code)
        C = H2H_to_C(tokens)
        return C

    def compile(self, input_path, output_path):
        H2H_code = read(input_path)
        H2H_to_C(H2H_code)
        write(output_path)
        return code

