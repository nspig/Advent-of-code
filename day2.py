input = """A Y
B X
C Z"""

with open('.\input\day2.txt') as f:
    input = f.read()

rounds = input.split ('\n')

def round(rnd):
    if rnd == 'A X': return 1 + 3
    elif rnd == 'A Y': return 2 + 6
    elif rnd == 'A Z': return 3 + 0
    elif rnd == 'B X': return 1 + 0
    elif rnd == 'B Y': return 2 + 3
    elif rnd == 'B Z': return 3 + 6
    elif rnd == 'C X': return 1 + 6
    elif rnd == 'C Y': return 2 + 0
    elif rnd == 'C Z': return 3 + 3
    else: return 0

print(sum(list(map(round, rounds))))

def round2(rnd):
    if rnd == 'A X': return 3 + 0
    elif rnd == 'A Y': return 1 + 3
    elif rnd == 'A Z': return 2 + 6
    elif rnd == 'B X': return 1 + 0
    elif rnd == 'B Y': return 2 + 3
    elif rnd == 'B Z': return 3 + 6
    elif rnd == 'C X': return 2 + 0
    elif rnd == 'C Y': return 3 + 3
    elif rnd == 'C Z': return 1 + 6
    else: return 0

print(sum(list(map(round2, rounds))))
