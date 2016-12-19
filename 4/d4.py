import re
from collections import Counter

def list_of_codes_from_string_input(codes):
  return list(filter(None, re.split('\s+', codes)))

def checksum_from_test_string(test):
  test = test.replace('-', '')
  pairs = sorted([(v, k) for k, v in Counter(test).items()], key = lambda x: (-x[0], x[1]))
  return ''.join(list(map(lambda x: x[1], pairs)))[0:5]

def sum_of_valid_sectors(codes):
  parsed_codes = list_of_codes_from_string_input(codes)
  sum_of_sectors = 0

  for code in parsed_codes:
    cypher = re.search('^([a-z\-]+)(\d+)\[([a-z]+)\]', code)

    test_string = cypher.group(1)
    sector      = int(cypher.group(2))
    checksum    = cypher.group(3)

    if checksum_from_test_string(test_string) == checksum:
      sum_of_sectors += sector

  return sum_of_sectors
