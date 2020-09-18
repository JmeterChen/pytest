# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2020-09-17


"""
需要安装 pytest-repeat 库
"""


import requests
import pytest


# 方式1：定义好的用例，执行时可以加上参数 --count=次数
def test_a():
	data = requests.get("http://127.0.0.1:8000/api/v1/product/")
	res = data.json() if data.status_code == 200 else {}
	assert res.get("code") == 1000


# @pytest.mark.repeat(10)
@pytest.mark.dependency(name='b')
def test_b():
	data = requests.get("http://127.0.0.1:8000/api/v1/product/")
	res = data.json() if data.status_code == 200 else {}
	assert res.get("code") == 1000
	

@pytest.mark.repeat(10)
@pytest.mark.dependency(depends=["b"])
def test_C():
	assert 1


