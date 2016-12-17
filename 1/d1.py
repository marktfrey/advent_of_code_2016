# State
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

def new_facing(facing, turn):
  return DIR_MAP[facing][turn]

def new_position(facing, distance, pos):
  if facing == 'N':
    return [pos[0] + distance, pos[1]]
  elif facing == 'E':
    return [pos[0], pos[1] + distance]
  elif facing == 'S':
    return [pos[0] - distance, pos[1]]
  elif facing == 'W':
    return [pos[0], pos[1] - distance]

def distance_from_origin(pos):
  return abs(pos[0]) + abs(pos[1])

def ending_position(path):
  facing   = 'N'
  position = [0, 0]

  for d in path.split(","):
    d = d.strip()
    turn     = d[0]
    distance = int(d[1: ])

    facing = new_facing(facing, turn)
    position = new_position(facing, distance, position)

  return position

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

def first_revisited_position(path):
  facing   = 'N'
  current_pos = [0, 0]
  past_pos    = [[0, 0]]

  for d in path.split(","):
    d = d.strip()
    turn     = d[0]
    distance = int(d[1: ])

    facing        = new_facing(facing, turn)
    new_positions = visited_positions(facing, distance, current_pos)

    for new_pos in new_positions:
      if new_pos in past_pos:
        return new_pos
      else:
        past_pos.append(new_pos)

    current_pos = past_pos[-1]
  return None

def first_revisited_distance_from_origin(path):
  first_pos = first_revisited_position(path)

  if first_pos is None:
    return None
  else:
    return distance_from_origin(first_pos)

def ending_distance_from_origin(path):
  pos = ending_position(path)
  return distance_from_origin(pos)
