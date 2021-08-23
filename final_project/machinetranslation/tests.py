import unittest
from machinetranslation.translator import *

class testing(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(englishToFrench('Hello'),'Bonjour')
    def test_bonjour(self):
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')
    def test_eng_null(self):
        self.assertEqual(englishToFrench(''),'')
    def test_fr_null(self):
        self.assertEqual(frenchToEnglish(''),'')

if __name__=='__main__':
    unittest.main()

