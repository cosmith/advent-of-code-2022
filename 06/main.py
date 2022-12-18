with open("input.txt") as f:
  string = list(f.read())

window_size = 14
window = [None] * window_size

for i in range(len(string) - window_size):
  for j in range(window_size):
    window[j] = string[i + j]
  if len(set(window)) == window_size:
    print(i + window_size)
    break
