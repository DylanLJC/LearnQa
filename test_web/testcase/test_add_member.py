"""
 根据业务逻辑编写，增加断言
 通过链式调用更加方便描述业务逻辑
"""
import pytest

from test_web.po.main_page import MainPage


class TestAddMember:
    @pytest.mark.parametrize("name", ["啦啦队正"])
    def test_add_member(self, name):
        main_page = MainPage()  # 初始化首页

        # #1跳转到addmamber页面
        # main_page.goto_addNumber()
        # 2添加一个成员，点击保存跳转到通讯录页面
        # 3在通讯录页面获取成员信息用于断言
        # 实现方法是通过链式调用
        #  main_page.goto_addNumber().add_member().goto_member_list()
        assert name in main_page.goto_addNumber().add_member().goto_member_list()
