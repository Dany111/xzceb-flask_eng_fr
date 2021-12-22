import unittest

from translator import english_to_french, french_to_english, language_translator

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english(0), 0)
        self.assertNotEqual(french_to_english('Null'),'')


class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french(0), 0)
        self.assertNotEqual(english_to_french('Null'),'')

        
unittest.main()