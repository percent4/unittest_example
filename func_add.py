# -*- coding: utf-8 -*-

# 根据传入数据类型不同，实现相加功能
def add(a, b):
    if isinstance(a, str) and isinstance(b, str):
        return a + '+' + b
    elif isinstance(a, list) and isinstance(b, list):
        return a + b
    elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    else:
        return None
