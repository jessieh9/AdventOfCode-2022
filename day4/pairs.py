file = open("day4/input.txt")
contents = file.readlines()
counter = 0

for i in contents:
    compare = []
    line = i.rstrip()  # 'xx-xx','xx-xx'
    pairs = line.split(',')  # contains the pairs ['xx-xx', 'xx-xx']
    for pair in pairs:
        # pair contains ['xx,xx'] and nums = [xx, xx]
        nums = [int(x) for x in pair.split('-')]
        for i in nums:
            compare.append(i)
    if (compare[2] >= compare[0] and compare[3] <= compare[1]):
        counter += 1
    elif (compare[0] >= compare[2] and compare[1] <= compare[3]):
        counter += 1

print(counter)
