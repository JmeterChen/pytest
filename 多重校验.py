# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2020-09-17

"""
需要安装 pytest-assume 库
"""


import pytest


def test_a():
        pytest.assume(3 == 3)
        pytest.assume(5 == 3)
        pytest.assume(4 == 4)
        pytest.assume(100 == 99)
