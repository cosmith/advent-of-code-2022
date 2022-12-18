from collections import defaultdict

with open("input.txt") as f:
    grid = [list(line) for line in list(f.read().splitlines())]

height = len(grid)
width = len(grid[0])

start = []
end = 0, 0

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == "S" or grid[y][x] == "a":
            start.append((x, y))
            grid[y][x] = "a"
        elif grid[y][x] == "E":
            end = x, y
            grid[y][x] = "z"

print(start, end)


def print_path(grid, visited):
    for y, line in enumerate(grid):
        for x, cell in enumerate(line):
            if (x, y) in visited:
                print(f"{cell}#", end="")
            else:
                print(cell, end=" ")
        print()
    print()


N = (0, -1)
S = (0, 1)
E = (1, 0)
W = (-1, 0)

tree = defaultdict(list)


def can_move(pos, direction):
    x, y = pos
    i, j = direction
    if x + i >= width or x + i < 0 or y + j >= height or y + j < 0:
        return False
    return ord(grid[y][x]) + 1 >= ord(grid[y + j][x + i])


def create_graph(grid):
    graph = defaultdict(list)
    for x in range(width):
        for y in range(height):
            for dir in [N, S, W, E]:
                next_cell = (x + dir[0], y + dir[1])
                if can_move((x, y), dir):
                    graph[(x, y)].append(next_cell)
    return graph


graph = create_graph(grid)


def bfs(graph, pos):
    visited = defaultdict(lambda: False)
    queue = [pos]
    visited[pos] = True
    distances = {pos: 0}
    predecessor = {}
    while len(queue) > 0:
        current = queue.pop(0)
        # if len(visited) % 20 == 0:
        #     print_path(grid, visited)
        for next in graph[current]:
            if not visited[next]:
                distances[next] = distances[current] + 1
                predecessor[next] = current
                queue.append(next)
                visited[next] = True
                if next == end:
                    return True, distances, predecessor
    return False, distances, predecessor


def get_shortest(graph, start):
    success, distances, predecessor = bfs(graph, start)

    if not success:
        print("no path found")
        return 100000

    path = {}
    current = end
    while current := predecessor.get(current):
        path[current] = True

    # print_path(grid, path)

    return max(distances.values())


print(min([get_shortest(graph, s) for s in start]))
