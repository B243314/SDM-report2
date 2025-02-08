#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):
#After Modifing
        def test_sample1 (self):
                self.assertEqual (0.02, calc(0.1,0.2))
        def test_sample2 (self):
                self.assertEqual (997002, calc(998,999))
        def test_sample3 (self):
                self.assertEqual (-1, calc(0,1))
        def test_sample4 (self):
                self.assertEqual (-1, calc(999,1000))
        def test_sample5 (self):
                self.assertEqual (-1, calc(999,998))
        def test_sample6 (self):
                self.assertEqual (-1, calc(5,5))        
        def test_sample7 (self):
                self.assertEqual (-1, calc(1001,2000))
        def test_sample8 (self):
                self.assertEqual (-1, calc('abc',5))
        def test_sample9 (self):
                self.assertEqual (-1, calc(5,'xyz'))
        def test_sample10 (self):
                self.assertEqual (-1, calc('ABC','XYZ'))
        def test_sample11 (self):
                self.assertEqual (-1, calc(-5,10))
        def test_sample12 (self):
                self.assertEqual (-1, calc(10,-5))
        def test_sample13 (self):
                self.assertEqual (-1, calc(-10,-5))
        def test_sample14 (self):
                self.assertEqual (3.75, calc(1.5,2.5))
