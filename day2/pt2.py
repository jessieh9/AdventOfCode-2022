def score(opp, me):
    if me == 'X':  # lose
        if (opp == 'A'):
            my_score = 3
        if (opp == 'B'):
            my_score = 1
        if (opp == 'C'):
            my_score = 2
        score = my_score + 0
        total.append(score)
    if me == 'Y':  # draw
        if (opp == 'A'):
            my_score = 1
        if (opp == 'B'):
            my_score = 2
        if (opp == 'C'):
            my_score = 3
        score = my_score + 3
        total.append(score)
    if me == 'Z':  # win
        if (opp == 'A'):
            my_score = 2
        if (opp == 'B'):
            my_score = 3
        if (opp == 'C'):
            my_score = 1
        score = my_score + 6
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
