from sys import argv
try:
    script, input_file = argv
except:
    print('input is not available')
try:
    file_handler = open(input_file, 'a+', encoding="utf-8")
    file_handler.seek(0, 0)
    line = file_handler.readline()
    stripped_line = line.strip()
    raw_bytes = stripped_line.encode("utf-8", errors="strict")
    print(f"printing: {stripped_line}")
    file_handler.seek(0, 2)
    file_handler.write(" blah blah")
except:
    print("file cannot be opened")
