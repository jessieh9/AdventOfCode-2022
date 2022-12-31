f = open("day7/test.txt")
commands = f.readlines()

directories = dict()
content = False
size = 0

def temporary(val, dir_dict):
    temp = 0
    for file in val:
        if not file.startswith("dir"):
            f = file.split(' ')
            temp += int(f[0])
        else:
            files = dir_dict[file[4:]]
            temp = temporary(files, dir_dict)
    return temp

def get_size(size, dir_dict):
    for val in dir_dict.values():
        temp = temporary(val, dir_dict)
        if temp <= 100000:
            size += temp
    return size

for c in commands:
    line = c.rstrip()
    if line.startswith("$ cd"):
        directories[line[5:]] = []
        current_dir = line[5:]
        continue
    if line.startswith("$ ls"):
        content = True
        continue
    if content:
        directories[current_dir].append(line)
print(directories)
print(get_size(size, directories))
        
