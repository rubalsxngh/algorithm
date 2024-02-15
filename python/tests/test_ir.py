import unittest
from information_retrievel import soundex



class test_soundex(unittest.TestCase):
    def test_sound(self):
        word1, word2= 'herman', 'hermun'

        ans= soundex.soundex(word1, word2)

        self.assertEqual(ans, 1)