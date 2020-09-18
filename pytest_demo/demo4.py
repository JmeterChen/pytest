# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2020-09-14

"""
对测试类参数化
"""

import pytest


def add(a, b):
	return a+b


# ids 的作用
data = [(1, 2, 3), (4, 5, 9), ('1', '2', '12'), ([11, 22], [33], [11, 22, 33])]
ids = [f'data{d}' for d in range(len(data))]  # => 生成与数据数量相同的名称列表


@pytest.mark.parametrize('a, b, c', data, ids=ids)
def test_add(a, b, c):
	# print(f'\na,b,c的值:{a},{b},{c}')
	assert add(a, b) == c