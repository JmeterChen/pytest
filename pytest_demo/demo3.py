# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2020-09-13


"""
对测试类参数化
"""

import pytest


def add(a, b):
	return a+b


# 测试类参数化
@pytest.mark.parametrize('a, b, c', [(1, 2, 3), (4, 5, 9)])
class TestAdd:
	def test_add1(self, a, b, c):
		assert add(a, b) == c

	def test_add2(self, a, b, c):
		assert add(a, b) == c