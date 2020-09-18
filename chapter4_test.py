# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2020-09-17

import pytest, requests


@pytest.mark.sf
@pytest.fixture()
def test_ddsf():
	url = 'https://ddsf.fangdd.com/data/login-loginByPassword'
	data = {
		"userName": "13217176556",
		"password": "123456"
	}
	expect = {"code": 200, "msg": "登录成功"}
	response = requests.post(url=url, json=data)
	res = response.json() if response.status_code == 200 else {}
	try:
		assert res.get("code") == expect["code"]
		assert res.get("msg") == expect["msg"]
	finally:
		return res


def test_success():
	res = test_ddsf
	assert res["msg"] == "登录成功"


if __name__ == '__main__':
	test_ddsf()