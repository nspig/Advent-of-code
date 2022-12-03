input = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""

with open('.\input\day1.txt') as f:
    input = f.read()

def process_elf(elf):
    elf = filter(None, elf.split('\n'))
    elf = map(lambda x: eval(x), elf)
    return sum(list(elf))

elves = input.split('\n\n')
# elves = list(map(lambda x: x.split('\n'), elves))
elves = list(map(process_elf, elves))
# print(max(elves))
elves.sort(reverse=True)
print(elves[0]+elves[1]+elves[2])
print(sum(elves[0:3]))