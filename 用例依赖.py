# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2020-09-17

"""
需要安装 pytest-dependency 库
"""

import pytest


#  在类下面实现依赖关系，第一种方式
class TestClass(object):

    @pytest.mark.dependency()
    # @pytest.mark.xfail(reason="deliberate fail")
    def test_a(self):
        assert True

    @pytest.mark.dependency()
    def test_b(self):
        pass

    @pytest.mark.dependency(depends=["TestClass::test_a"])
    def test_c(self):
        pass

    @pytest.mark.dependency(depends=["TestClass::test_b"])
    def test_d(self):
        pass

    @pytest.mark.dependency(depends=["TestClass::test_b", "TestClass::test_c"])
    def test_e(self):
        pass


#  在类下面实现依赖关系，第二种方式
class TestClassNamed(object):

    @pytest.mark.dependency(name="a")
    #   @pytest.mark.xfail(reason="deliberate fail")
    def test_a(self):
        assert False

    @pytest.mark.dependency(name="b", depends=["a"])
    def test_b(self):
        pass

    @pytest.mark.dependency(name="c")
    def test_c(self):
        pass

    @pytest.mark.dependency(name="d", depends=["c"])
    def test_d(self):
        pass

    @pytest.mark.dependency(name="e", depends=["b", "c"])
    def test_e(self):
        pass