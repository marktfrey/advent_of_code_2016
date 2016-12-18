import re

def valid_triangle_sides(triple):
  sides = list(map(int, filter(None, re.split('\s+', triple))))
  a = sides[0]
  b = sides[1]
  c = sides[2]

  return (a + b > c, a + c > b, b + c > a).count(True) == 3

def valid_triangle_count_from_triples(triples):
  triples = list(filter(lambda x: re.match('^\s*$', x) == None, re.split('\n', triples)))
  valids = map(valid_triangle_sides, triples)
  return list(valids).count(True)
