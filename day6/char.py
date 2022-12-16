import sys

f = open("day6/input.txt")
contents = f.readlines()
# line = contents[0].rstrip()
line = "bvwbjplbgvbhsrlpgdmjqwftvncz"
char = 0
within = True

# bvw bjplbgvbhsrlpgdmjqwftvncz
for ind, l in enumerate(line):  # b    vwbjplbgvbhsrlpgdmjqwftvncz
    while line != '':
        temp = ind
        check = line[0:4]  # bjpl
        print(check)
        c_copy = check
        for c in c_copy:  # b  vwb
            if c in check:
                char += 1 # 3
                
                line = line[temp+1:]
                print(line)
                break
            else:
                char += 1
                within = False
                print(char)
