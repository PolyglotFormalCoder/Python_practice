from sys import argv
script, input_encoding, error = argv


def main(language_file, encoding, errors):
    line = language_file.readline()
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, error1):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=error1)
    cooked_string = raw_bytes.decode(encoding, errors=error1)
    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)