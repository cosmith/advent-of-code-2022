from pprint import pprint
from collections import defaultdict
import math
import re

with open("input.txt") as f:
  instructions = list(f.read().splitlines())

x = 1
cycle = 0


def printcycle(cycle, x):
  # part 1
  # if (cycle + 20) % 40 == 0:
  #   print(cycle, x)
  #   result[0] += x * cycle
  
  # part 2
  if cycle % 40 in [x - 1, x, x + 1]:
    print("#", end="")
  else:
    print(".", end="")

  if (cycle + 1) % 40 == 0:
    print("")


for instruction in instructions:
  printcycle(cycle, x)
  cycle += 1
  
  if instruction == "noop":
    continue
  else:
    printcycle(cycle, x)
    cycle += 1

    x += int(instruction.split(" ")[1])
