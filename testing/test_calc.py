from python_code.calc import Calculator


class TestCalc:
    def setup_class(self):
        print("开始计算")
        # 将实例化的对象放在setup 上
        self.calc = Calculator()

    def teardown_class(self):
        print("计算结束")

    def test_add(self):
        # # 实例化计算器的类
        # calc = Calculator()
        # 调用add方法
        result = self.calc.add(1, 1)
        # 得到结果用断言
        assert result == 2


def test_sub():
    pass


def test_mul():
    pass


def test_div():
    pass
