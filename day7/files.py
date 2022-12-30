f = open("day7/test.txt")
commands = f.readlines()

directories = dict()

for c in commands:
    line = c.rstrip()
    if "cd" in line:
        directories[line[5:]] 
        
