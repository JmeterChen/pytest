# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2020-09-17

"""
pytest-rerunfailures
"""

import pytest
import requests
import time


# reruns是重跑次数，reruns_delay是间隔时间
@pytest.mark.dependency(name="a")
@pytest.mark.flaky(reruns=5, reruns_delay=2)
def test_a():
	try:
		data = requests.get("http://127.0.0.1:8000/api/v1/product/")
		res = data.json() if data.status_code == 200 else {}
		assert res.get("code") == 1000
	except Exception as e:
		assert False


@pytest.mark.dependency(depends=["a"])
def test_b():
	assert 1