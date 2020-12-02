f = open("C:\\Users\\marquina\\Documents\\GitHub\\adventofcode2020\\02\\02.txt")

mins = 0
maxs = 0
char = ''
strs = ''
valids = 0

def isvalid_silver(_min, _max, _char, _str):
    valid = 0
    for c in _str:
        if c == _char:
            valid = valid + 1
    return ((valid >= _min) and (valid <= _max))

def isvalid_gold(_min, _max, _char, _str):
    valid = 0
    for c in range(len(_str)):
        if c == _min - 1:
            if _str[c] == _char:
                valid = valid + 1
        elif c == _max - 1:
            if _str[c] == _char:
                valid = valid + 1
    return (valid == 1)

for i in f:
    temporal = i.split(":")
    strs = (temporal[1].strip())
    temporal = temporal[0].split(" ")
    char = (temporal[1])
    temporal = temporal[0].split("-")
    mins = temporal[0].strip()
    maxs = temporal[1].strip()
    if isvalid_gold(int(mins), int(maxs), char, strs):
        print("Min {} Max {} Char {} Str {}".format(mins, maxs, char, strs))
        valids = valids + 1

print("Valid inputs are {}".format(valids))