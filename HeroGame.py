# 2-1作业第一次提交，后面会继续再次提交一次

# 创建一个英雄类
class Hero:
    name = "default"
    hp = 0
    power = 0

    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power

    def fight(self, enemy_hp, enemy_power):  # 敌人的血量，敌人的攻击力

        my_final_hp = self.hp - enemy_power
        enemy_final_hp = enemy_hp - self.power

        if my_final_hp > enemy_final_hp:
            print(f"恭喜您，您的英雄{self.name}赢了")
        elif my_final_hp < enemy_final_hp:
            print(f"很抱歉，您的英雄{self.name}输了")
        else:
            print("平局")


def main():
    print("本游戏属于回合制游戏,该游戏只打一回合")
    # 实例化英雄
    Hero1 = Hero('timo', 500, 12)
    Hero2 = Hero('Police', 600, 11)

    HeroNumber = input("本轮游戏你可以选择以下两种英雄:1 timo  2 police ,请输入一个英雄编号选择英雄:")
    HeroNumber = int(HeroNumber)

    if HeroNumber == 1:
        print(f"您选择的英雄是: {Hero1.name},您的敌人是：{Hero2.name}")
        Hero1.fight(Hero2.hp, Hero2.power)
    elif HeroNumber == 2:
        print(f"您选择的英雄是: {Hero2.name},您的敌人是：{Hero1.name}")
        Hero2.fight(Hero1.hp, Hero1.power)
    else:
        print("不好意思请重新选择")


if __name__ == '__main__':
    main()
