with open('Input/Q4.txt') as f:
     data = f.read()
     data = data.split('\n\n')

def validateField(field, value):
  if field == 'byr':
    if int(value) < 1920 or int(value) > 2002:
      return False
  elif field == 'iyr':
    if int(value) < 2010 or int(value) > 2020:
      return False
  elif field == 'eyr':
    if int(value) < 2020 or int(value) > 2030:
      return False
  elif field == 'hgt':
    measure = 'cm' if 'cm' in value else 'in'
    value = int(value.replace('cm', '').replace('in', ''))
    if measure == 'cm':
      if value < 150 or value > 193:
        return False
 
    elif measure == 'in':
      if value < 59 or value > 76:
        return False

  elif field == 'hcl':
    if value[0] != '#':
      return False
    for char in value[1:]:
      if not (char.isdigit() or (ord('a') <= ord(char) <= ord('f'))):
        return False 

  elif field == 'ecl':
    colours = ['amb', 'blu', 'brn' ,'gry', 'grn', 'hzl', 'oth']
    if value not in colours:
      return False

  elif field == 'pid':
    if len(value) != 9 or not value.isnumeric():
      return False

  return True

part1=0
reqFields=['byr','iyr','eyr','hgt','hcl','ecl','pid']
for entry in data:
  numFields=0
  fields = entry.split()
  for field in fields:
    if field.split(':')[0] in reqFields: 
      numFields+=1
  if numFields == 7:
    part1+=1

part2=0
for entry in data:
  numFields=0
  fields = entry.split()
  for field in fields:
    if field.split(':')[0] in reqFields and validateField(field.split(':')[0], field.split(':')[1]): 
      numFields+=1
  if numFields == 7:
    part2+=1

print("Part 1: ", part1)
print("Part 2: ", part2)