import sys

read_lines = sys.stdin.readlines()
line_to_be_read = [line for line in read_lines if not (line[0] == '>')]
line_to_be_read = [line.lower() for line in line_to_be_read]

for line in line_to_be_read:
    new_line = ""
    if(len(line)>10000):
        new_line = "BP length too long (over 10,000)"
    else: 
        for i in line:
            match i: 
                case 'a':
                    new_line += 'T'
                case 't':
                    new_line += 'A'
                case 'g':
                    new_line += 'C'
                case 'c':
                    new_line += 'G'

    sys.stdout.write(">SEQ_ID\n" + new_line + "\n")

