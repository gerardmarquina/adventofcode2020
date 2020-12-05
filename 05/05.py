file_input = open("C:\\users\\root\\Documents\\GitHub\\adventofcode2020\\05\\05.txt")

sanitized_input = []

for line in file_input:
    sanitized_input.append(line.strip().replace("B", "1").replace("F", "0").replace("R", "1").replace("L", "0"))

binaries = []

for bins in sanitized_input:
    binaries.append(int(bins, 2))

print(max(binaries)) # Part 1
print(next(ms for ms in range(int("1111111111", 2) + 1) if (ms not in binaries and ms-1 in binaries and ms+1 in binaries))) # Part 2