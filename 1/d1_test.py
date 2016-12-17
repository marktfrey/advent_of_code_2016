import d1
import unittest

class AdventOfCodeDay1TestCase(unittest.TestCase):
  
  known_values = (
                   ('R2, L3', 5),
                   ('R2, R2, R2', 2),
                   ('R5, L5, R5, R3', 12)
                 )

  def test_ending_distance_from_origin(self):
    for path, expected in self.known_values:
       result = d1.ending_distance_from_origin(path)
       self.assertEqual(expected, result)

if __name__ == '__main__':
  unittest.main()