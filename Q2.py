with open('Input/Q2.txt') as f:
  data = [line for line in f]

# part 1
part1 = 0
for line in data:
  entries = line.split()
  
  numbers = entries[0].split(sep='-')
  min = int(numbers[0])
  max = int(numbers[1])
  
  letter = entries[1][0]
  pw = entries[2]

  if min <= pw.count(letter) <= max:
    part1 += 1

# part 2
part2 = 0
for line in data:
  entries = line.split()

  numbers = entries[0].split(sep='-')
  pos1 = int(numbers[0])
  pos2 = int(numbers[1])

  letter = entries[1][0]
  pw = entries[2]

  if (pw[pos1-1] == letter and pw[pos2-1] != letter) or (pw[pos1-1] != letter and pw[pos2-1] == letter):
    part2 += 1

print("Part 1: ", part1)
print("Part 2: ", part2)