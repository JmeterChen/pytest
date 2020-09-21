# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2020-09-20


def test_success(login, teardown, close_):
	assert login["msg"] == "登录成功"


def test_success1(login, teardown, close_):
	assert login["msg"] == "登录成功"


class TestDemo1:
	
	def test_success2(self, login, teardown, close_):
		assert login["msg"] == "登录成功"
	
	def test_success3(self, login, teardown, close_):
		assert login["msg"] == "登录成功1"
	
	def test_success4(self, login, close_):
		assert login["msg"] == "登录成功2"
	
	def test_success5(self, login, close_):
		assert login["msg"] == "登录成功2"