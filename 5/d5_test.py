import d5
import unittest

class AdventOfCodeDay5TestCase(unittest.TestCase):

  def test_passcode_from_string(self):
    code = "abc"

    result = d5.passcode_from_string(code, 8)
    self.assertEqual('18f47a30', result)

  def test_better_passcode_from_string(self):
    code = "abc"

    result = d5.better_passcode_from_string(code, 8)
    self.assertEqual('05ace8e3', result)

if __name__ == '__main__':
  unittest.main()
