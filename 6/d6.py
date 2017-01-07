import re
from collections import Counter

def parse_lines_from_string(code):
  return list(filter(None, re.split('\s+', code)))

def columns_from_rows(rows):
  output = []
  for pos in range(0, len(rows[0])):
    output.append([])
    for row in rows:
      output[pos].append(row[pos])

  return output

def letter_frequency(col, inverse=False):
  rev = not inverse
  return sorted([(v, k) for k, v in Counter(col).items()], reverse = rev)

def signal_from_string(code, inverse_frequency=False):
  rows = parse_lines_from_string(code)
  columns = columns_from_rows(rows)

  return ''.join([letter_frequency(col, inverse_frequency)[0][1] for col in columns])
