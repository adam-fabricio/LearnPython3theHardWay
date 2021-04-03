"""Exercício 23 - Stringsm Bytes, and Character Encodings."""


import sys
script, input_encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding,errors=errors)

    print(raw_bytes, "<===>", cooked_string)

languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)

breaking_it3 = b'Rewrite this using the b\'\' bytes instead of the UTF-8 strings effectievely reversing the script'
teste = "'''   . , "
print(teste.encode())
print(breaking_it3.decode().encode())

