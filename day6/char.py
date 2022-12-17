f = open("day6/input.txt")
contents = f.readlines()
line = contents[0].rstrip()

num = 4
while True:
    # set because it will remove duplicates - no duplicates means len of 4
    if len(set(line[:4])) != 4:  # bvwbjplb gvbhsrlpgdmjqwftvncz
        line = line[1:]
        num += 1
    else:
        break
print(num)
