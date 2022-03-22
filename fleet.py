from robots import Robot
from weapon import Weapon
class Fleet:
    def __init__(self) :
        self.robots = []
        self.create_fleet()
    
    def create_fleet(self):
        weapon1 = Weapon("Flaming Sword", 50)
        weapon2 = Weapon("Frozen Potato Gun", 50)
        weapon3 = Weapon("Gravity Gun", 50)

        robot1 = Robot("Megabuzz", weapon1)
        robot2 = Robot("Lightyear", weapon2)
        robot3 = Robot("Julius", weapon3)

        self.robots.append(robot1)
        self.robots.append(robot2)
        self.robots.append(robot3)
