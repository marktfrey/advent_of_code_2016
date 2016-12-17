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

def ending_distance_from_origin(path):
  pos = ending_position(path)
  return distance_from_origin(pos)
