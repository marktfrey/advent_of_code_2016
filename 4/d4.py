import re

def list_of_codes_from_string_input(codes):
  out = list(filter(None, re.split('\s+', codes)))
  print(out)
  return out

def sum_of_valid_sectors(codes):
  list_of_codes_from_string_input(codes)
  return None