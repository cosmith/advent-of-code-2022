def get_ord(char):
  if ord(char) <= 90:
    return ord(char) - 38
  return ord(char) - 96


with open("input.txt") as f:
  lines = f.read().splitlines()

length = len(lines)
i = 0

badges = 0

while i < length:
  badge = (set(lines[i])
    .intersection(set(lines[i+1]))
    .intersection(set(lines[i+2])))
  badges += get_ord(list(badge)[0])
  i += 3

print(badges)