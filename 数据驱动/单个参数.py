# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2020-09-13


"""
pytest 中的参数化， 类似unittest中的ddt
"""

import pytest


def add(a, b):
	return a+b


@pytest.mark.parametrize("a", (100, 200, 300, 400))
def test_add(a):
	print(f"\na的值为：{a}")
	assert add(a, 1) == a+1


