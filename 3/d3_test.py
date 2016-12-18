import d3
import unittest

class AdventOfCodeDay3TestCase(unittest.TestCase):

  def test_valid_triangle_count_from_triples(self):
    triangles = """
      3  4  5
      5 10 25
    """

    result = d3.valid_triangle_count_from_triples(triangles)
    self.assertEqual(1, result)


if __name__ == '__main__':
  unittest.main()
