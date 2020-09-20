# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2020-09-20


import pytest, requests


@pytest.fixture()
def login():
	url = 'https://ddsf.fangdd.com/data/login-loginByPassword'
	data = {
		"userName": "13217176556",
		"password": "123456"
	}
	expect = {"code": 200, "msg": "登录成功"}
	response = requests.post(url=url, json=data)
	res = response.json() if response.status_code == 200 else {}
	print("login success")
	try:
		assert res.get("code") == expect["code"]
		assert res.get("msg") == expect["msg"]
	finally:
		return res


@pytest.fixture()
def teardown():
	yield
	print("测试结束，断开连接！")