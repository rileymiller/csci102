


n = int(input('enter n'))

y = 0

while y < n:
    roll = random.randInt(1,6)

    if roll == 1:
        rolls[1] += 1

for i in range(1,6):
    print('OUTPUT ' + str(i) + ' occured ' + rolls[i])
