file = open('file.txt', 'r')
file_read = file.read()
duels = file_read.splitlines()
file.close()
key = []
skills_after = []

for duel in duels:
    inputs = duel.split(" > ")
    for input in inputs:
        if input not in key:
            key.append(input)
skills_after = [[0 for _ in range(len(key))]for _ in range(len(key))]
for duel in duels:
    inputs = duel.split(" > ")
    for index, input in enumerate(inputs):
        try:
            skills_after[key.index(input)][key.index(inputs[index+1])] += 1
        except IndexError:
            pass
for i in range(len(key)):
    total = 0
    for j in range(len(key)):
        total += skills_after[i][j]
    for j in range(len(key)):
        try:
            skills_after[i][j] =  round(skills_after[i][j]/total,4)
        except ZeroDivisionError:
            skills_after[i][j] = 0
        if skills_after[i][j] == 0.0:
            skills_after[i][j] = 0
        if skills_after[i][j] == 1.0:
            skills_after[i][j] = 1
for i in range(len(key)):
    total = 0
    for j in range(len(key)):
        total += skills_after[i][j]
    if total!=1:
        for j in range(len(key)):
            if skills_after[i][j] != 0:
                skills_after[i][j] = round(skills_after[i][j]+(1-total),4)
                break

print("[",end="")
for i in range(len(key)):
    print("[",end="")
    for j in range(len(key)):
        print(str(skills_after[i][j]),end="")
        if j!=len(key)-1:
            print(",",end="")
    if i==len(key)-1:
        print("]]")
    else:
        print("],")