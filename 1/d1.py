DIR_MAP = {
    'N':
      { 'R': 'E',
        'L': 'W' },
    'E':
      { 'R': 'S',
        'L': 'N' },
    'S':
      { 'R': 'W',
        'L': 'E' },
    'W':
      { 'R': 'N',
        'L': 'S' }
  }

def distance_from_origin(pos):
  return None if pos is None else abs(pos[0]) + abs(pos[1])

def visited_positions(facing, distance, pos):
  visited = []

  for i in range(1, distance + 1):
    if facing == 'N':
      visited.append([pos[0] + i, pos[1]])
    elif facing == 'E':
      visited.append([pos[0], pos[1] + i])
    elif facing == 'S':
      visited.append([pos[0] - i, pos[1]])
    elif facing == 'W':
      visited.append([pos[0], pos[1] - i])

  return visited

def traversal(path):
  facing      = 'N'
  prior_pos   = [[0, 0]]

  for d in path.split(","):
    d = d.strip()
    facing    =  DIR_MAP[facing][d[0]]
    prior_pos += visited_positions(facing, int(d[1: ]), prior_pos[-1])

  return prior_pos

def first_revisited_position(path):
  visited = traversal(path)
  for i, pos in enumerate(visited):
    if pos in visited[0:i]:
      return pos
  return None

def ending_distance_from_origin(path):
  pos = traversal(path)[-1]
  return distance_from_origin(pos)

def first_revisited_distance_from_origin(path):
  pos = first_revisited_position(path)
  return distance_from_origin(pos)
