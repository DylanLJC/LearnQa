import pytest
import yaml

from python_code.calc import Calculator

# with open("./cacle.yaml.") as f:
#     add_datas = yaml.safe_load(f)['add']
# 独立于类之外，定义一个全局的
with open("./cacle.yaml.") as f:  # 定义一个参数f
    datas = yaml.safe_load(f)['add']  # 寻找到yaml中的数据
    add_datas = datas['datas']  # 寻找到datas的值
    print(add_datas)
    myid = datas['myid']  # 给datas起名字
    print(myid)


class TestCalc:

    def setup_class(self):
        print("开始计算")
        # 实例化计算器的类
        self.calc = Calculator()  # 实例变量

    def teardown_class(self):
        print("计算结束")

    # @pytest.mark.parametrize("a,b,excpect",
    #                          [(1,1,2),
    #                           (2,2,4),
    #                           (0.1,0.1,0.2)],
    #                           ids=["int","int","flout"])#ids 自己指定的用例名称
    @pytest.mark.parametrize("a,b,excpect",
                             add_datas, ids=myid)
    def test_add(self, a, b, excpect):
        # 调用add方法
        result = self.calc.add(a, b)  # 增加一个self
        # 得到结果用断言
        assert result == excpect

    # def test_add1(self):
    #
    #     # 调用add方法
    #     result = self.calc.add(1, 2)  #增加一个self
    #     # 得到结果用断言
    #     assert result == 3
    # def test_add2(self):
    #
    #     # 调用add方法
    #     result = self.calc.add(5, 1)  #增加一个self
    #     # 得到结果用断言
    #     assert result == 6


def test_sub():
    pass


def test_mul():
    pass


def test_div():
    pass
