import re

KEYPAD = (
  (1, 2, 3),
  (4, 5, 6),
  (7, 8, 9)
)

def value_from_position(pos):
  return KEYPAD[pos[1]][pos[0]]

def position_from_direction(d, pos):
  if d is 'U':
    return [pos[0], max(pos[1] - 1, 0)]
  elif d is 'R':
    return [min(pos[0] + 1, len(KEYPAD[pos[1]]) - 1), pos[1]]
  elif d is 'D':
    return [pos[0], min(pos[1] + 1, len(KEYPAD) - 1)]
  elif d is 'L':
    return [max(pos[0] - 1, 0), pos[1]]

def code_from_instructions(instructions):
  pos  = [1, 1]
  code = 0
  instructions = list(filter(None, re.split('\s+', instructions)))

  for instruction in instructions:
    code *= 10
    for d in instruction:
      pos = position_from_direction(d, pos)
    code += value_from_position(pos)

  return code
