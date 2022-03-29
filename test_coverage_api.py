# -*- coding: utf-8 -*-
import coverage
import unittest

if __name__ == '__main__':

    cov = coverage.Coverage()
    cov.start()

    # 测试套件
    suite = unittest.defaultTestLoader.discover("./", "test_func_add.py")
    unittest.TextTestRunner().run(suite)

    cov.stop()
    cov.save()

    cov.html_report(directory='test_func_add')
