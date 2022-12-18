import re

# test.txt
# stacks = [['Z', 'N'], ['M', 'C', 'D'], ['P']]

# input.txt
stacks = [list(stack) for stack in [
  'FDBZTJRN',
  'RSNJH',
  'CRNJGZFQ',
  'FVNGRTQ',
  'LTQF',
  'QCWZBRGN',
  'FCLSNHM',
  'DNQMTJ',
  'PGS'
]]


with open("input.txt") as f:
  lines = f.read().splitlines()

reg = re.compile(r"move (\d+) from (\d+) to (\d+)")

for line in lines:
  if len(line) == 0 or line[0] != "m":
    continue
  matches = reg.match(line)
  count = int(matches.group(1))
  origin = int(matches.group(2)) - 1
  destination = int(matches.group(3)) - 1

  temp = []
  for _ in range(count):
    temp.insert(0, stacks[origin].pop())
  stacks[destination].extend(temp)

print("".join([s[-1] for s in stacks]))