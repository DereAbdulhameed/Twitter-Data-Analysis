import unittest
import sys


sys.path.append(r'C:\Users\HP\Desktop\10Academy\Twitter-Data-Analysis\TESTINGDEMO\tests_\scripts')
from sample_script import find_average

class TestSimpleScript(unittest.TestCase):

    def test_find_average(self):
        expected = 1
        actual = find_average(1, 1)
        self.assertEqual(actual, expected)


    def test_divide_num(self):
        expected = 2
        actual = divide_num(4, 2)
        self.assertEqual(expected, actual)

