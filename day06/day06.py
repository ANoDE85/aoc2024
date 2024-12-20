print("Day06")

def load_matrix(fn):
    with open(f"day06/{fn}") as f:
        data = [
            [c for c in line.strip()] for line in f.readlines()
        ]
    return data

data = load_matrix('input.txt')

def up(pos):
    return (pos[0]-1, pos[1])

def right(pos):
    return (pos[0], pos[1]+1)

def down(pos):
    return (pos[0]+1, pos[1])

def left(pos):
    return (pos[0], pos[1]-1)

commands = [up, right, down, left]

curr_dir = 0
positions = set()
for row_idx, row in enumerate(data):
    if '^' in row:
        curr_pos = (row_idx, row.index('^'))
        positions.add(curr_pos)
        break
done = False
while True:
    while True:
        new_pos = commands[curr_dir](curr_pos)
        if new_pos[0] < 0 or new_pos[0] >= len(data) or new_pos[1] > len(data[0]) or new_pos[1] < 0:
            # we have moved off the map, exit
            done = True
            break
        if data[new_pos[0]][new_pos[1]] in ('.', '^'):
            positions.add(new_pos)
            curr_pos = new_pos
            break
        else:
            curr_dir = (curr_dir + 1) % len(commands)
    if done:
        break
print(len(positions))


# Part 2

data = load_matrix('input.txt')
start_pos = None
for row_idx, row in enumerate(data):
    if '^' in row:
        curr_pos = (row_idx, row.index('^'))
        start_pos = curr_pos
        break

# this time we'll store the position AND the trajectory we've traversed this spot already.
# if we hit a spot with the same trajectory we already hit it before, we're in a loop
def traverse(matrix, positions):
    curr_dir = 0
    curr_pos = start_pos
    while True:
        while True:
            new_pos = commands[curr_dir](curr_pos)
            if new_pos[0] < 0 or new_pos[0] >= len(matrix) or new_pos[1] >= len(matrix[0]) or new_pos[1] < 0:
                # we have moved off the map, exit
                return False
            if matrix[new_pos[0]][new_pos[1]] in ('.', '^'):
                if new_pos in positions and curr_dir in positions[new_pos]:
                    # we found a loop
                    return True
                positions.setdefault(new_pos, []).append(curr_dir)
                curr_pos = new_pos
                break
            else:
                curr_dir = (curr_dir + 1) % len(commands)

# We only need to traverse the spots we saw in the first run,
# since the guard will never step on the others without our modification
# (and there's only one modification, so no need to be iterative)
# This removes many possible spots and makes this complete faster :)
count = 0
for spot in positions:
    if spot == start_pos:
        continue
    new_matrix = [
            [c for c in row] for row in data
        ]
    new_matrix[spot[0]][spot[1]] = 'O'
    if traverse(new_matrix, {start_pos : [0]}):
        count += 1
print(count)

