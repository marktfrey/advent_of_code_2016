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

    self.assertEqual('easter', d6.signal_from_string(code))
    self.assertEqual('advent', d6.signal_from_string(code, True))

if __name__ == '__main__':
  unittest.main()
