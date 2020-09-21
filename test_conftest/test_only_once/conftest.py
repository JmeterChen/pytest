# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2020-09-20


import pytest, requests


@pytest.fixture(scope='session')
def login():
	url = 'https://ddsf.fangdd.com/data/login-loginByPassword'
	data = {
		"userName": "13217176556",
		"password": "123456"
	}
	expect = {"code": 200, "msg": "登录成功"}
	response = requests.post(url=url, json=data)
	res = response.json() if response.status_code == 200 else {}
	print("登录成功，测试开始！")
	try:
		assert res.get("code") == expect["code"]
		assert res.get("msg") == expect["msg"]
	finally:
		return res


@pytest.fixture(scope='session')
def teardown():
	yield
	print("测试结束，断开连接！")
	
	
@pytest.fixture()
def close_(request):
	print("测试已经结束！")
	
	def fin1():
		print("准备调用close1函数！")
		
	def fin2():
		print("准备调用close2函数！")
		
	request.addfinalizer(fin1)
	request.addfinalizer(fin2)
	return close_