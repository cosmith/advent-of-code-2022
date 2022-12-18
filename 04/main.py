
with open("input.txt") as f:
  lines = f.read().splitlines()

contained = 0
overlap = 0
for line in lines:
  elf1, elf2 = line.split(',')
  l1,r1 = (int(x) for x in elf1.split('-'))
  l2,r2 = (int(x) for x in elf2.split('-'))

  if (l1 <= l2 and r1 >= r2) or (l2 <= l1 and r2 >= r1):
    contained += 1

  if not (r1 < l2 or r2 < l1):
    overlap += 1

print(contained, overlap)