import d2
import unittest

class AdventOfCodeDay2TestCase(unittest.TestCase):

  def test_code_from_instructions(self):
    input_string = """ULL RRDDD LURDL UUUUD"""
    expected     = 1985

    result = d2.code_from_instructions(input_string)
    self.assertEqual(expected, result)

if __name__ == '__main__':
  unittest.main()
