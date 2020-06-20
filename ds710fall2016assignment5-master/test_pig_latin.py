import unittest
import pig_latin as p

class TestPig(unittest.TestCase):

    def test_names(self):
        self.assertEqual(p.say_piglatin('crystal'), 'ystalcray')
        self.assertEqual(p.say_piglatin('try'), 'ytray')
        self.assertEqual(p.say_piglatin('quarter'), 'arterquay')
        self.assertEqual(p.say_piglatin('pig'), 'igpay')
        self.assertEqual(p.say_piglatin('Latin'), 'Atinlay')
        self.assertEqual(p.say_piglatin('trash'), 'ashtray')

if __name__ == '__main__':
    unittest.main()
