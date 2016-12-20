import re
import hashlib

def passcode_from_string(code, length):
  i = 0
  passcode = []

  while len(passcode) < length:
    salted_int = (code + str(i)).encode('utf-8')
    md5_hash = hashlib.md5(salted_int).hexdigest()
    match = re.match('^00000([a-f0-9])', md5_hash)

    if match is not None:
      passcode.append(match.group(1))

    i += 1

  return ''.join(passcode)
    
def better_passcode_from_string(code, length):
  i = 0
  passcode = [None for i in range(0, length)]

  while None in passcode:
    salted_int = (code + str(i)).encode('utf-8')
    md5_hash = hashlib.md5(salted_int).hexdigest()
    exp = '^00000([0-' + str(length - 1) + '])([a-f0-9])'
    match = re.match(exp, md5_hash)
    if match is not None:
      code_index = int(match.group(1))
      if passcode[code_index] is None:
        passcode[code_index] = match.group(2)

    if (i % 5000 == 0):
      display = format_passcode(passcode, md5_hash)
      print("  Determining passcode: %(display)s (with cinematic display)" % locals(), end="\r")
    i += 1

  display = format_passcode(passcode, md5_hash)
  print("              passcode: %(display)s" % locals(), end="\n")
  return ''.join(passcode)

def format_passcode(passcode, md5_hash):
  RS = '\x1b[3;37;41m'
  GS = '\x1b[0;30;42m'
  CE = '\x1b[0m'

  display = ''
  for j in range(0, len(passcode)):
    if passcode[j]:
      display += GS + passcode[j] + CE
    else:
      display += RS + md5_hash[j] + CE

  return display
      