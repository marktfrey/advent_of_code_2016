import d2
import d2p2
import unittest

class AdventOfCodeDay2TestCase(unittest.TestCase):

  def test_d2_code_from_instructions(self):
    input_string = """ULL RRDDD LURDL UUUUD"""
    expected     = 1985

    result = d2.code_from_instructions(input_string)
    self.assertEqual(expected, result)

  def test_d2p2_code_from_instructions(self):
    input_string = """ULL RRDDD LURDL UUUUD"""
    expected     = '5DB3'

    result = d2p2.code_from_instructions(input_string)
    self.assertEqual(expected, result)

if __name__ == '__main__':
  unittest.main()
