# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2020-09-13


import pytest


def add(a, b):
	return a+b


@pytest.mark.parametrize('a, b, c', [(1, 2, 3), (4, 5, 9), ('1', '2', '12')])
def test_add(a, b, c):
	"""
	多个参数
	"""
	assert add(a, b) == c
	print(f"\na, b, c的值分别为：{a}, {b}, {c}")
	
	
# 测试类参数化
@pytest.mark.parametrize('a, b, c', [(1, 2, 3), (4, 5, 9)])     # 括号中的第一个字符串参数一定要和下面的函数参数一致
class TestAdd:
	"""
	对测试类参数化
	"""
	def test_add1(self, a, b, c):
		assert add(a, b) == c

	def test_add2(self, a, b, c):
		assert add(a, b) == c