import sys

lines_of_data = sys.stdin.readlines()

ans = ""
header = ">SEQ_ID\n"

ind = 0
for line in lines_of_data:
    if(ind % 4 == 1):
        ans += header
        ans += line
    ind += 1

sys.stdout.write(ans)