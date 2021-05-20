import pytest


def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 5


def test_answer1():
    assert inc(4) == 5


class TestDemo:
    # def __init__(self):   不能有init方法
    def test_a(self):
        print("a")

    def test_b(self):
        print("b")

    def test_c(self):
        print("c")


if __name__ == '__main__':
    pytest.main(['test_sample.py :: TestDemo'])
