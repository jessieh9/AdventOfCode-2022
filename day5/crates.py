# [H]                 [Z]         [J]
# [L]     [W] [B]     [G]         [R]
# [R]     [G] [S]     [J] [H]     [Q]
# [F]     [N] [T] [J] [P] [R]     [F]
# [B]     [C] [M] [R] [Q] [F] [G] [P]
# [C] [D] [F] [D] [D] [D] [T] [M] [G]
# [J] [C] [J] [J] [C] [L] [Z] [V] [B]
# [M] [Z] [H] [P] [N] [W] [P] [L] [C]
#  1   2   3   4   5   6   7   8   9

f = open("day5/move.txt", "r")
content = f.readlines()
s = ""

start = {1:list("HLRFBCJM"), 2:list("DCZ"), 3: list("WGNCFJH"), 
4: list("BSTMDJP"), 5: list("JRDCN"), 
6:list("ZGJPQDLW"), 7:list("HRFTZP"), 
8:list("GMVL"), 9:list("JRQFPGBC")}

#part 1
for i in content:
    line = i.rstrip() # move 3 from 2 to 1
    y = line.split("move ")[1].split(" from ") #[3, "2 to 1"]
    numbers = y[1].split(" to ") #[2, 1]

    contents = [int(y[0])] # [3]
    contents.extend(numbers) #[3, '2', '1']
    contents = [int(j) for j in contents] #[3, 2, 1]
    
    # move the stacks from one column to the next 
    movingstacks = start[contents[1]][:contents[0]][::-1] #[Z, C, D]
    start[contents[2]] = movingstacks + start[contents[2]] #[Z, C, D] + list("HLRFBCJM")

    # clear the stack from the original column
    start[contents[1]] = start[contents[1]][contents[0]:]

for key in start:
    s += start[key][0]
print(s)