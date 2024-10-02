# test_module1.py

import unittest
import module1


class TestModule1(unittest.TestCase):
    def test_dospely(self):
        hodnoty = [18, 50]
        for vek in hodnoty:
            result = module1.je_dospely(vek, 'CZ')
            self.assertTrue(result)

    def test_dospely_18(self):
        result = module1.je_dospely(18, 'CZ')
        self.assertTrue(result)

    def test_dospely_50(self):
        result = module1.je_dospely(50, 'CZ')
        self.assertTrue(result)
    
    def test_dospely_17(self):
        result = module1.je_dospely(17, 'CZ')
        self.assertEqual(result, False)
    
    def test_dospely_0(self):
        result = module1.je_dospely(0, 'CZ')
        self.assertEqual(result, False)
    
    def test_dospely_negative(self):
        with self.assertRaises(ValueError):
            module1.je_dospely(-1, 'CZ')


class TestModule1_US(unittest.TestCase):
    def test_dospely_18(self):
        result = module1.je_dospely(18, 'US')
        self.assertEqual(result, False)

    def test_dospely_21(self):
        result = module1.je_dospely(21, 'US')
        self.assertTrue(result)
    
    def test_dospely_20(self):
        result = module1.je_dospely(20, 'US')
        self.assertEqual(result, False)

unittest.main()
