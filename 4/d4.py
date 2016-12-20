import re
from collections import Counter
import string

def list_of_codes_from_string_input(codes):
  return list(filter(None, re.split('\s+', codes)))

def dict_from_cypher(cypher):
  split_cypher = re.search('^([a-z\-]+)(\d+)\[([a-z]+)\]', cypher)
  return {
           'code_string': split_cypher.group(1),
           'sector':      int(split_cypher.group(2)),
           'checksum':    split_cypher.group(3)
         }

def decrypt_test_string_with_key(code, key):
  alpha = 'abcdefghijklmnopqrstuvwxyz'
  alpha_key = key%len(alpha)
  new_alpha = alpha[alpha_key:] + alpha[:alpha_key]
  return code.translate(str.maketrans(alpha, new_alpha)).replace('-', ' ')

def checksum_from_test_string(test):
  test = test.replace('-', '')
  pairs = sorted([(v, k) for k, v in Counter(test).items()], key = lambda x: (-x[0], x[1]))
  return ''.join(list(map(lambda x: x[1], pairs)))[0:5]

def sum_of_valid_sectors(codes):
  parsed_codes = list_of_codes_from_string_input(codes)
  sum_of_sectors = 0

  for code in parsed_codes:
    d = dict_from_cypher(code)

    if checksum_from_test_string(d['code_string']) == d['checksum']:
      sum_of_sectors += d['sector']

  return sum_of_sectors

def output_valid_sector_names(codes):
  parsed_codes = list_of_codes_from_string_input(codes)
  for code in parsed_codes:
    d = dict_from_cypher(code)
    if checksum_from_test_string(d['code_string']) == d['checksum']:
      sector = d['sector']
      solution = decrypt_test_string_with_key(d['code_string'], sector)
      print("'%(solution)s' : %(sector)s" % locals())
