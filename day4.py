input="""2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

with open('.\input\day4.txt') as f:
    input = f.read() 

def make_range(s):
    left, right= s.split("-")
    return set(range(int(left), int(right)+1))

def parse_line(line):
    left, right= line.split(",")
    left= make_range (left)
    right = make_range(right)
    return (left, right)

lines= input.split("\n")
# lines=list(map(lambda x: x.split(","), lines))
lines = list(map(parse_line, lines))

x = list(filter(lambda x: x[0].issubset(x[1]) or x[1].issubset(x[0]), lines))
print (len(x))

x = list(filter(lambda x: x[0].intersection(x[1]), lines))
print (len(x))