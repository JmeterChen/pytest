# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2020-09-17


import pytest
import requests


def f():
	raise SystemExit(1)


def test_mytest():
	with pytest.raises(SystemExit):
		f()


def test_01():
	print(111)


# 将多个用例放在一个class中
class TestClass:
	def test_one(self):
		x = "this"
		print("test_one")
		assert "h"  in x
	
	# def test_awo(self):
	# 	x = 'hello'
	# 	print("test_awo")
	# 	assert hasattr(x, "check")
	
	@pytest.mark.sf
	def test_ddsf(self):
		url = 'https://ddsf.fangdd.com/data/login-loginByPassword'
		data = {
			"userName": "13217176556",
			"password": "123456"
		}
		expect = {"code": 200, "msg": "登录成功"}
		response = requests.post(url=url, json=data)
		res = response.json() if response.status_code == 200 else {}
		assert res.get("code") == expect["code"]
		assert res.get("msg") == expect["msg"]
		
	@pytest.mark.sf
	def test_ddsf2(self):
		url = 'https://ddsf.fangdd.com/data/login-loginByPassword'
		data = {
			"userName": "13217176556",
			"password": "123456"
		}
		expect = {"code": 200, "msg": "登录成功"}
		response = requests.post(url=url, json=data)
		res = response.json() if response.status_code == 200 else {}
		assert res.get("code") == expect["code"]
		assert res.get("msg") == expect["msg"]
		
	@pytest.mark.sf
	def test_ddsf3(self):
		url = 'https://ddsf.fangdd.com/data/login-loginByPassword'
		data = {
			"userName": "13217176556",
			"password": "123456"
		}
		expect = {"code": 200, "msg": "登录成功"}
		response = requests.post(url=url, json=data)
		res = response.json() if response.status_code == 200 else {}
		assert res.get("code") == expect["code"]
		assert res.get("msg") == expect["msg"]
		
	@pytest.mark.sf
	def test_ddsf4(self):
		url = 'https://ddsf.fangdd.com/data/login-loginByPassword'
		data = {
			"userName": "13217176556",
			"password": "123456"
		}
		expect = {"code": 200, "msg": "登录成功"}
		response = requests.post(url=url, json=data)
		res = response.json() if response.status_code == 200 else {}
		assert res.get("code") == expect["code"]
		assert res.get("msg") == expect["msg"]
		
	@pytest.mark.sf
	def test_ddsf5(self):
		url = 'https://ddsf.fangdd.com/data/login-loginByPassword'
		data = {
			"userName": "13217176556",
			"password": "123456"
		}
		expect = {"code": 200, "msg": "登录成功"}
		response = requests.post(url=url, json=data)
		res = response.json() if response.status_code == 200 else {}
		assert res.get("code") == expect["code"]
		assert res.get("msg") == expect["msg"]


def test_needsfiles(a):
	print(a)
	assert 0
	

def test_add():
	assert 100 + 200 == 300