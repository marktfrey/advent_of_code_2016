import re

KEYPAD = (
(None, None, 1, None, None),
(None, 2, 3, 4, None),
(5, 6, 7, 8, 9),
(None, 'A', 'B', 'C', None),
(None, None, 'D', None, None)
)

def val_at(pos):
  return KEYPAD[pos[1]][pos[0]]

def position_from_direction(d, pos):
  x = pos[0]
  y = pos[1]

  if d is 'U':
    yp = max(y - 1, 0)
    y = y if val_at([x, yp]) is None else yp
  elif d is 'R':
    xp = min(x + 1, len(KEYPAD[y]) - 1)
    x = x if val_at([xp, y]) is None else xp
  elif d is 'D':
    yp = min(y + 1, len(KEYPAD) - 1)
    y = y if val_at([x, yp]) is None else yp
  elif d is 'L':
    xp = max(x - 1, 0)
    x = x if val_at([xp, y]) is None else xp

  return [x, y]

def code_from_instructions(instructions):
  pos  = [0, 2]
  code = []
  instructions = list(filter(None, re.split('\s+', instructions)))

  for instruction in instructions:
    for d in instruction:  
      pos = position_from_direction(d, pos)   
    code.append(str(val_at(pos)))

  return ''.join(code)
