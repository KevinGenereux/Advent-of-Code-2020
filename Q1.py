from itertools import combinations

with open('Input/Q1.txt') as f:
  data = [int(line) for line in f]

# Part 1
for combo in combinations(data,2):
  if combo[0] + combo[1] == 2020:
    part1 = combo[0]*combo[1]

# Part 2
for combo in combinations(data,3):
  if combo[0] + combo[1] + combo[2] == 2020:
    part2 = combo[0] * combo[1] * combo[2]

print("Part 1: ", part1)
print("Part 2: ", part2)