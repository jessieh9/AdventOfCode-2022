file = open("day4/input.txt")
contents = file.readlines()
counter = 0

for i in contents:
    one = []
    two = []
    compare = []
    line = i.rstrip()  # 'xx-xx','xx-xx'
    pairs = line.split(',')  # contains the pairs ['xx-xx', 'xx-xx']
    for pair in pairs:
        # pair contains ['xx,xx'] and nums = [xx, xx]
        nums = [int(x) for x in pair.split('-')]
        for i in nums:
            compare.append(i)
    for i in range(compare[0], compare[1]+1):
        one.append(i)

    for j in range(compare[-2], compare[-1]+1):
        two.append(j)
    
    for x in one:
        if x in two:
            counter += 1
            break

print(counter)
