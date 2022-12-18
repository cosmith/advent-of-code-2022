with open("input.txt") as f:
  lines = [L.strip() for L in f.readlines()]

elves = []
currentsum = 0
for line in lines:
  if line == "":
    elves.append(currentsum)
    currentsum = 0
    continue
  calories = int(line)
  currentsum += calories

print(sum(sorted(elves, reverse=True)[:3]))