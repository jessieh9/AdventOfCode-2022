def score(opp, me):
    if me == 'X':
        my_score = 1
    if me == 'Y':
        my_score = 2
    if me == 'Z':
        my_score = 3
    if (opp == 'A' and me == 'Z') or (opp == 'B' and me == 'X') or (opp == 'C' and me == 'Y'):  # loses
        score = my_score + 0
        total.append(score)
    elif (me == 'Y' and opp == 'A') or (me == 'X' and opp == 'C') or (me == 'Z' and opp == 'B'):  # wins
        score = my_score + 6
        total.append(score)
    else:
        score = my_score + 3
        total.append(score)
    return total

file = open("day2/strat.txt")
content = file.readlines()
total = []

for i in range(len(content)):
    s = content[i].rstrip()
    opp = s[0]
    my_play = s[2]
    score(opp, my_play)
print(sum(total))
