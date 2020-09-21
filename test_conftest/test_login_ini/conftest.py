# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2020-09-21

import pytest

# conftest.py


@pytest.fixture(autouse=True)
def fuc_fix(pytestconfig):
	# print(pytestconfig.getini('markers'))
	# print(pytestconfig.getini('log_cli'))
	return pytestconfig.getini('markers')