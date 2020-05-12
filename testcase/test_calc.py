# -*- coding:utf-8 -*-
import pytest
from duanming_auto_test.pytest_testwork.basic.calc import Calc
import yaml
import sys

from decimal import *

getcontext().prec = 2

sys.path.append('../')


class TestCalc:
    def setup(self):
        self.calc = Calc
        # print('../data/calc.yaml')

    @pytest.mark.parametrize(["x", "y", "result"], yaml.safe_load(open("../data/calc.yaml")))
    def test_add(self, x, y, result):
        try:

            calc_add = self.calc.add(Decimal(x), Decimal(y))
            print(calc_add)
            assert calc_add == result
        except TypeError:
            return print("类型错误")

    # @pytest.mark.parametrize(["x", "y", "result"], yaml.safe_load(open("../data/calc.yaml")))
    # def test_subtract(self, x, y, result):
    #     calc_subtract = self.calc.subtract(x, y)
    #     assert calc_subtract == result
    #
    # @pytest.mark.parametrize(["x", "y", "result"], yaml.safe_load(open("../data/calc.yaml")))
    # def test_multiply(self, x, y, result):
    #     calc_multiply = self.calc.multiply(x, y)
    #     assert calc_multiply == result

    @pytest.mark.parametrize(["x", "y", "result"], yaml.safe_load(open("../data/calc_div.yaml")))
    def test_divide(self, x, y, result):
        try:
            calc_divide = self.calc.divide(x, y)
            assert calc_divide == result
        except ZeroDivisionError:
            return print("除数不能为0")
        except TypeError:
            return print("不能为字符")


if __name__ == '__main__':
    pytest.main('-vs')
