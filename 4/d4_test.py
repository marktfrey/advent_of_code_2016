import d4
import unittest

class AdventOfCodeDay4TestCase(unittest.TestCase):

  def test_valid_rooms_sector_sum(self):
    codes = """
      aaaaa-bbb-z-y-x-123[abxyz]
      a-b-c-d-e-f-g-h-987[abcde]
      not-a-real-room-404[oarel]
      totally-real-room-200[decoy]
    """

    result = d4.sum_of_valid_sectors(codes)
    self.assertEqual(1514, result)

  def test_decrypt_test_string(self):
    code = "qzmt-zixmtkozy-ivhz"
    key  = 343

    result = d4.decrypt_test_string_with_key(code, key)
    self.assertEqual('very encrypted name', result)

if __name__ == '__main__':
  unittest.main()
