# -*- coding: utf-8 -*-
import unittest

from func_add import add


class TestAdd(unittest.TestCase):
    def setUp(self):
        pass

    def test_add_case1(self):
        a = "Hello"
        b = "World"
        res = add(a, b)
        print(res)
        self.assertEqual(res, "Hello+World")

    def test_add_case2(self):
        a = 1
        b = 2
        res = add(a, b)
        print(res)
        self.assertEqual(res, 3)

    def test_add_case3(self):
        a = [1, 2]
        b = [3]
        res = add(a, b)
        print(res)
        self.assertEqual(res, [1, 2, 3])

    def test_add_case4(self):
        a = 2
        b = "3"
        res = add(a, b)
        print(None)
        self.assertEqual(res, None)
