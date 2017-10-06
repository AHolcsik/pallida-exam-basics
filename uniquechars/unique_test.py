import unittest
import unique_chars

class AnagramTest(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(unique_chars.unique_characters(''),[])

    def test_one_letter(self):
        self.assertEqual(unique_chars.unique_characters('a'), ['a'])

    def test_one_letter(self):
        self.assertEqual(unique_chars.unique_characters('aa'), [])


if __name__ == '__main__':
    unittest.main()
