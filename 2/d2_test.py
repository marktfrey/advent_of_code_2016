import d2
import unittest

class AdventOfCodeDay2TestCase(unittest.TestCase):
  
  known_values = (
                   ( """
                     ULL
                     RRDDD
                     LURDL
                     UUUUD
                     """, 1985)
                 )

  def test_code_from_instructions(self):
    for instructions, expected in self.known_values:
       result = d2.code_from_instructions(instructions)
       self.assertEqual(expected, result)

if __name__ == '__main__':
  unittest.main()
