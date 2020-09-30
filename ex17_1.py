from sys import argv

script, file_name = argv

file_1 = open(file_name, 'w+')

data = file_1.read()

print(data)

#file_1.close()

#file_1 = open(file_name, 'w')

file_1.truncate()

input_1 = input(">")

file_1.write(input_1)

file_1.close()