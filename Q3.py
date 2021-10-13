with open('Input/Q3.txt') as f:
  data = [line[0:-1] for line in f]

def Traverse(right, bottom):
  row=0
  col=0
  count=0

  numRows = len(data)
  numCols = len(data[0])

  while row < numRows:
    if data[row][col] == '#':
      count += 1
    
    row += bottom
    col += right

    if col >= numCols:
      col -= numCols

  return count

part1 = Traverse(3, 1)
part2 = Traverse(1, 1) * Traverse(3, 1) * Traverse(5, 1) * Traverse(7, 1) * Traverse(1, 2)

print("Part 1: ", part1)
print("Part 2: ", part2)