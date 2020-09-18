# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2020-09-13


"""
多个参数
"""

import pytest


def add(a, b):
	return a+b


@pytest.mark.parametrize('a, b, c', [(1, 2, 3), (4, 5, 9), ('1', '2', '12')])
def test_add(a, b, c):
	assert add(a, b) == c
	print(f"\na, b, c的值分别为：{a}, {b}, {c}")