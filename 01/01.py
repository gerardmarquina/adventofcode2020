abs_path = "C:\\Users\\marquina\\Documents\\GitHub\\adventofcode2020\\01\\01.txt"

file_input = open(abs_path)

# remove duplicates
l = []
for i in file_input:
    if i not in l: 
        l.append(int(i))

l.sort() # small numbers = high possibility of being part of the result

for i in l:
    for j in l:
        for k in l:
            if (i + j + k) == 2020:
                print("Gold solution is {}".format(i*j*k))
        if (i + j) == 2020:
            print("Silver solution is {}".format(i * j))

# Not optimized at all but works