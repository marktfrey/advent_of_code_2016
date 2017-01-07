import d6
import unittest

class AdventOfCodeDay6TestCase(unittest.TestCase):

  def test_signal_from_string(self):
    code = """
           eedadn
           drvtee
           eandsr
           raavrd
           atevrs
           tsrnev
           sdttsa
           rasrtv
           nssdts
           ntnada
           svetve
           tesnvt
           vntsnd
           vrdear
           dvrsen
           enarar
           """

    result = d6.signal_from_string(code)
    self.assertEqual('easter', result)

if __name__ == '__main__':
  unittest.main()
