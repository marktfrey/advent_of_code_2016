import d3
import unittest

class AdventOfCodeDay3TestCase(unittest.TestCase):

  def test_valid_triangle_count_from_horizontal_triples(self):
    triangles = """
      3  4  5
      5 10 25
    """

    result = d3.valid_triangle_count_from_horizontal_triples(triangles)
    self.assertEqual(1, result)

  def test_valid_triangle_count_from_verical_triples(self):
    triangles = """
      3  5  8
      4 10  8
      5 25  8
      5  7  6
     10  8  8
     25  9 10
    """

    result = d3.valid_triangle_count_from_vertical_triples(triangles)
    self.assertEqual(4, result)


if __name__ == '__main__':
  unittest.main()
