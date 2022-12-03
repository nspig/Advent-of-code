input="""vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

with open('.\input\day3.txt') as f:
    input = f.read() 

def get_common(item):
    left = set(item[:len(item) // 2])
    right = set(item[len(item) // 2:])
    # print(left & right)
    return list(left & right)[0]

def convert(letter):
    o=ord(letter)
    if o >= ord('a') and o <= ord('z'):
        o -= 96
    else:
        o-=38
    # print(letter, o)
    return o

sacks = input.split("\n")
# print (sacks)

print(sum(map(convert, map(get_common, sacks))))

def lina_chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

def get_common_p2(items):
    first = set(items[0])
    second = set(items[1])
    third = set(items[2])
    return list(first & second & third)[0]

n=5
x = list(lina_chunks(sacks, 3))
# print (x)
x = sum(map(convert, map(get_common_p2, x)))
print(x)
# print (list mapget_common_p2(x))
