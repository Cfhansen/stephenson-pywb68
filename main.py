###solution to exercise 68 from ben stephenson's "the python workbook".

import re
pattern = re.compile('[01]{8}')

def get_bit():
  print("Enter a string of 8 bits:")
  result = input()
  if re.match(pattern,result):
    return str(result)
  else:
    print('That\'s not a valid string.')

bit = get_bit()

if bit:
  parity = bit.count('1') % 2
  if parity:
    print('This string has odd parity.')
  else:
    print('This string has even parity.')
