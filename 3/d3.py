import re
import math

def valid_triangle_sides(triple):
  a = triple[0]
  b = triple[1]
  c = triple[2]

  return (a + b > c, a + c > b, b + c > a).count(True) == 3

def string_triple_to_int_list(triple):
  return list(map(int, filter(None, re.split('\s+', triple))))

def valid_triangle_count_from_horizontal_triples(triples):
  triples = list(filter(lambda x: re.match('^\s*$', x) == None, re.split('\n', triples)))
  int_triples = list(map(string_triple_to_int_list, triples))
  valids = map(valid_triangle_sides, int_triples)
  return list(valids).count(True)

def chunk_list(l, size):
    res = []
    for i in range(0, math.ceil(len(l)/size)):
      s = len(res) * size
      e = (len(res) * size) + size
      res.append(l[s:e])
    return res

def valid_triangle_count_from_vertical_triples(triples):
  string_triples = list(filter(lambda x: re.match('^\s*$', x) == None, re.split('\n', triples)))
  int_triples = list(map(string_triple_to_int_list, string_triples))

  columns = list(zip(*int_triples))
  chunked_columns = [chunk_list(l, 3) for l in columns]

  triples = []
  for column in chunked_columns:
    for chunk in column:
      triples.append(chunk)

  valids = map(valid_triangle_sides, triples)
  return list(valids).count(True)
