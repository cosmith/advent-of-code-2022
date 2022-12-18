games = []

corr = {
  'A': 'r',
  'B': 'p',
  'C': 's',
  ' ': '',
  '\n': '',
  'X': 'X',
  'Y': 'Y',
  'Z': 'Z'
}

with open("input.txt") as f:
  for line in f.readlines():
    games.append("".join([corr[c] for c in line]))

scores = {
  'r': {'r': 3, 'p': 6, 's': 0},
  'p': {'r': 0, 'p': 3, 's': 6},
  's': {'r': 6, 'p': 0, 's': 3}
}
shapes = {'r': 1, 'p': 2, 's': 3}

moves = {
  'r': {'X': 's', 'Y': 'r', 'Z': 'p'},
  'p': {'X': 'r', 'Y': 'p', 'Z': 's'},
  's': {'X': 'p', 'Y': 's', 'Z': 'r'},
}

score = 0
for game in games:
  opp = game[0]
  play = game[1]
  mine = moves[opp][play]
  # print(scores[opp][mine]+shapes[mine])
  score += scores[opp][mine]+shapes[mine]

print(score)
