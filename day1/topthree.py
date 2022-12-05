# Dec 01, 2022 - Solve for the top three highest total calories that the elf is carrying

file = open("day1/elves.txt")
content = file.readlines()  # list containing lines of the file
cals = 0
temp_list = []
pos = 0
start = 0
cal_list = []
max_three = []

for i in range(len(content)):
    if content[i].rstrip() != '':
        temp_list.append(int(content[i].rstrip()))
        pos += 1
    else:  # if it is a space
        start = pos
        pos = 0
        temp_list = []
    cal_list.append(sum(temp_list))
    if sum(temp_list) > cals:
        cals = sum(temp_list)
print(cals)
print()
for i in range(3):
    m = max(cal_list)
    max_three.append(m)
    cal_list.remove(m)
print(sum(max_three))
file.close()
