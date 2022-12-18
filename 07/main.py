from pprint import pprint
from collections import defaultdict
import re

with open("input.txt") as f:
  lines = list(f.read().splitlines())

print(lines)

tree = {}

starts_with_num = re.compile(r"^([0-9]+) (.*)$")


def set(dic, path, key, value):
  if len(path) == 0:
    dic[key] = value
    return
  if dic.get(path[0]) is None:
    dic[path[0]] = {}
  return set(dic[path[0]], path[1:], key, value)


current_path = []
for line in lines:
  if "$ cd /" in line:
    current_path = []
  elif "$ cd .." in line:
    current_path.pop()
  elif "$ cd" in line:
    dir = line.replace("$ cd ", "")
    current_path.append(dir)
  elif match := starts_with_num.match(line):
    size = int(match.group(1))
    name = match.group(2)
    set(tree, current_path, name, size)

grand_total = [999999999999]

available_space = 70000000
needed_space = 30000000

dirsizes = []


def size(dir, key="/"):
  total = 0
  for k, v in dir.items():
    if type(v) == dict:
      total += size(v, k)
    else:
      total += v
  dirsizes.append((k, total))
  return total


to_free = size(tree) - (available_space - needed_space)

dirsizes = sorted(dirsizes, key=lambda x: x[1])

print("to free", to_free)
print("dirsizes", dirsizes)

for (dir, size) in dirsizes:
  if size > to_free:
    print(dir, size)
    break