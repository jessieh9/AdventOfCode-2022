f = open("day6/input.txt")
contents = f.readlines()
line = contents[0].rstrip()

num = 14
while True:
    # set because it will remove duplicates - no duplicates means len of 14
    if len(set(line[:14])) != 14:
        line = line[1:]
        num += 1
    else:
        break
print(num)
