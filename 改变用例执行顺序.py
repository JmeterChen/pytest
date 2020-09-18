# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2020-09-17


"""
需要安装 pytest-ordering 库
"""

import pytest


# 先执行test_b再执行test_a
@pytest.mark.run(order=2)
def test_a():
	print(11111)
	assert False


@pytest.mark.run(order=1)
def test_b():
	print(22222)
	assert not 1
	
	
@pytest.mark.run(order=0)
def test_c():
	print("00000")
	assert 0