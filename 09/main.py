from pprint import pprint
from collections import defaultdict
import math
import re

with open("input.txt") as f:
    moves = list(f.read().splitlines())

rope = [[0, 0] for _ in range(10)]

directions = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}

visited = set()


def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    return 0


def move_tail(tail, head):
    distance = (tail[0] - head[0]) ** 2 + (tail[1] - head[1]) ** 2
    if distance > 2:
        tail[0] += sign(head[0] - tail[0])
        tail[1] += sign(head[1] - tail[1])
    return [tail[0], tail[1]]


def grid(size, rope):
    for y in range(size - 1, -size, -1):
        print("")
        for x in range(-size, size):
            for item in rope:
                if (x, y) == item:
                    print("H", end="")
            if (x, y) == (0, 0):
                print("s", end="")
            else:
                print(".", end="")
    print("")


for move in moves:
    direction, magnitude = move.split(" ")
    magnitude = int(magnitude)
    print("\n\n---", direction, magnitude)
    for step in range(magnitude):
        rope[0][0] += directions[direction][0]
        rope[0][1] += directions[direction][1]
        for i in range(1, len(rope)):
            rope[i] = move_tail(rope[i], rope[i - 1])
        visited.add(tuple(rope[-1]))
    # grid(20, rope)


print(len(list(visited)))
