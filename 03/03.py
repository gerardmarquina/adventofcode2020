f = open("C:\\Users\\root\\Desktop\\aoc\\03.txt")

m =[[]]

for lines in f:
  line = []
  for char in range(len(lines) - 1):
      line.append(lines[char].strip())
  m.append(line)

m.remove([])
currentx = 0
currenty = 0
tree = 0

while currenty < len(m)-1:
  currentx = currentx + 1 # For part two just modify this 
  currenty = currenty + 2 # lines and multiply the results
  if currentx >= len(m[0]):
    currentx = currentx - len(m[0])
  #print("Checking Y{} X{} which is {}".format(currenty, currentx, m[currenty][currentx]))
  if m[currenty][currentx] == "#":
    tree = tree + 1
      
print(tree)