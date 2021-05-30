import pytest
import yaml

from python_code.calc import Calculator

with open('./cacleSubmit.yaml', 'r', encoding='UTF-8') as f:
    datas = yaml.safe_load(f)['cacle']  # 寻找到yaml中的数据
    add_cacle = datas['add']  # 寻找到datas的值
    add_datas = add_cacle['datas']
    ymalName = add_cacle['myid']

    datasDiv = datas['div']
    add_datasDiv = datasDiv['datas']
    ymalNameDiv = datasDiv['myid']


class TestCalc:

    def setup_class(self):
        print('开始计算')
        self.calc = Calculator()

    def teardown_class(self):
        print('计算结束')

    @pytest.mark.parametrize("a,b,excption", add_datas, ids=ymalName)
    def test_add(self, a, b, excption):
        result = self.calc.add(a, b)
        assert result == excption

    @pytest.mark.parametrize("a,b,excption", add_datasDiv, ids=ymalNameDiv)
    def test_div(self, a, b, excption):
        result = self.calc.div(a, b)
        assert result == excption
     ###
