# Dec 01, 2022 - Solve for the highest total calories that the elf is carrying

file = open("elves.txt")
content = file.readlines()  # list containing lines of the file
cals = 0
temp_list = []
pos = 0
start = 0

for i in range(len(content)):
    if content[i].rstrip() != '':
        temp_list.append(int(content[i].rstrip()))
        pos += 1
    else:  # if it is space
        start = pos
        pos = 0
        temp_list = []
    if sum(temp_list) > cals:
        cals = sum(temp_list)
print(cals)
file.close()
