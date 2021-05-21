# 简单工厂方法
from HeroGame1 import EZ, Jinx, Timo


def create_hero(hero):
    if hero == "ez":
        return EZ()
    elif hero == "jinx":
        return Jinx()
    elif hero == "Timo":
        return Timo()
    else:
        raise Exception("工厂内没有多余的英雄")
