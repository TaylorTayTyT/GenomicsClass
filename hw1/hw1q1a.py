import fileinput

lines_of_data = fileinput.input()
#print(type(lines_of_data))  # fileinput.FileInput

for line in lines_of_data:
    print(line)