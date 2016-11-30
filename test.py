import unittest
from exam4 import greeter

class ExamUnittest(unittest.TestCase):
    # def __init__(self):
    #     pass
    def test_empyt_input(self):
        self.assertEqual(greeter(""), 'Hello, Mr Nobody!')

    def test_for_char(self):
        self.assertEqual(greeter("a"), 'Hello, a!')

    def test_number_for_input(self):
        self.assertEqual(greeter(11), 'Hello, 11!')

    def test_number_error(self):
        self.assertRaises(TypeError,greeter,11)

    def test_list_for_input(self):
        self.assertEqual(greeter(["letmepass","this","exam"]), 'Hello, Mr Nobody!')

    def test_list_for_input_error(self):
        self.assertRaises(TypeError, greeter, ["letmepass","this","exam"])

if __name__ == '__main__':
    unittest.main()
