from pprint import pprint
from collections import defaultdict
import re

with open("input.txt") as f:
  trees = list(f.read().splitlines())

trees = [[int(x) for x in list(line)] for line in trees]

size = len(trees)

# part 1
# visible = [[0] * size for _ in range(size)]

# for i in range(0, size):
#   highestL = -1
#   highestR = -1
#   highestT = -1
#   highestB = -1
#   for j in range(0, size):
#     if trees[i][j] > highestL:
#       highestL = trees[i][j]
#       visible[i][j] = 1
#     if trees[i][size - j - 1] > highestR:
#       highestR = trees[i][size - j - 1]
#       visible[i][size - j - 1] = 1
#     if trees[j][i] > highestT:
#       highestT = trees[j][i]
#       visible[j][i] = 1
#     if trees[size - j - 1][i] > highestB:
#       highestB = trees[size - j - 1][i]
#       visible[size - j - 1][i] = 1

# print(sum([sum(x) for x in visible]))

# part 2
scenic = [[0] * size for _ in range(size)]

maxscenic = 0

for i in range(size):
  for j in range(size):
    visibilityT = 0
    visibilityB = 0
    y = 1
    while i - y >= 0:
      visibilityT += 1
      if trees[i - y][j] >= trees[i][j]:
        break
      y += 1
    y = 1
    while i + y < size:
      visibilityB += 1
      if trees[i + y][j] >= trees[i][j]:
        break
      y += 1
    visibilityL = 0
    visibilityR = 0
    x = 1
    while j - x >= 0:
      visibilityL += 1
      if trees[i][j - x] >= trees[i][j]:
        break
      x += 1
    x = 1
    while j + x < size:
      visibilityR += 1
      if trees[i][j + x] >= trees[i][j]:
        break
      x += 1
    scenic[i][j] = visibilityT * visibilityB * visibilityL * visibilityR
    maxscenic = max(scenic[i][j], maxscenic)

pprint(scenic)
print(maxscenic)
