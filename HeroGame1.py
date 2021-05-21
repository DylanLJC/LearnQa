# 定义一个英雄类

class Hero():
    my_hp = 0
    my_power = 0
    my_name = 'a'

    def fight(self, enemy_hp, enemy_power):
        my_final_hp = self.my_power - enemy_hp
        enemy_final_power = enemy_power - self.my_hp
        if my_final_hp > enemy_final_power:
            print(f"恭喜您，您的英雄{self.my_name}")
        elif my_final_hp < enemy_final_power:
            print(f"很抱歉，您的英雄{self.my_name}输了")
        else:
            print("平局了")


# 建立子类

class Jinx(Hero):
    my_hp = 1000
    my_power = 210
    my_name = 'jinx'


class EZ(Hero):
    my_hp = 1000
    my_power = 190
    my_name = 'ez'


class Timo(Hero):
    my_hp = 1020
    my_power = 190
    my_name = 'Timo'


jinx = Jinx()
ez = EZ()
