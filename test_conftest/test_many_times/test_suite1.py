# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2020-09-20


def test_success(login):
	assert login["msg"] == "登录成功"


def test_success1(login):
	assert login["msg"] == "登录成功"


class TestDemo1:
	
	def test_success2(self, login, teardown):
		assert login["msg"] == "登录成功"
	
	def test_success3(self, login, teardown):
		assert login["msg"] == "登录成功"
	
	def test_success4(self, login, teardown):
		assert login["msg"] == "登录成功"
	
	def test_success5(self, login, teardown):
		assert login["msg"] == "登录成功"