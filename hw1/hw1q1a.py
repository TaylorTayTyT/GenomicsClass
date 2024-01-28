import sys
def convert_to_FASTA(input):
    lines_of_data = input

    ans = ""
    header = ">SEQ_ID\n"

    ind = 0
    for line in lines_of_data:
        if(ind % 4 == 1):
            ans += header
            ans += line
        ind += 1

    sys.stdout.write(ans)

convert_to_FASTA(sys.stdin.readlines())