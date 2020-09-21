# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2020-09-21

import pytest
import json, requests


# @pytest.fixture(scope="session")
def get_data():
	with open("data.json", "r", encoding="utf-8") as d:
		data = json.load(d)
		print("ok")
	return data


class TestParam:
	
	url = 'https://ddsf.fangdd.com/data/login-loginByPassword'
	
	@pytest.mark.parametrize("data", get_data())
	def test_login(self, data):
		response = requests.post(url=self.url, json=data[0])
		res = response.json()
		assert res.get("code") == data[1].get("code")
		assert res.get("msg") == data[1].get("msg")