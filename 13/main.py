import json
from functools import cmp_to_key


with open("input.txt") as f:
  lines = list(f.read().splitlines())
lines.append("")

def compare(l, r):
  if type(l) == int and type(r) == int:
    if l == r:
      return None
    elif l < r:
      return -1
    else:
      return 1

  if type(l) == list and type(r) == list:
    if len(l) == len(r) == 0:
      return None
    if len(l) > 0 and len(r) == 0:
      return 1
    elif len(l) == 0:
      return -1
    else:
      ret = compare(l[0], r[0]) 
      if ret is not None:
        return ret
      return compare(l[1:], r[1:])

  elif type(l) == int and type(r) == list:
    return compare([l], r)

  elif type(l) == list and type(r) == int:
    return compare(l, [r])

to_sort = [[[2]], [[6]]]

for i in range(0, len(lines) // 3):
  left = json.loads(lines[i * 3])
  right = json.loads(lines[i * 3 + 1])
  to_sort += [left, right]

result = sorted(to_sort, key=cmp_to_key(compare))

signal = 1
for i in range(len(result)):
  if result[i] in ([[2]], [[6]]):
    signal *= (i + 1)

print(signal)