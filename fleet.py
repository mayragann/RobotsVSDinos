from robots import Robot
from weapon import Weapon


class Fleet:
    def __init__(self):
        self.robots = []
        self.create_fleet()


    def create_fleet(self):
        weapon_one = Weapon("Burning Sword", 50)
      

        robot_one= Robot("Tinkerbell the Robot", weapon_one)
        robot_two = Robot("Charming the Robot", weapon_one)
        robot_three= Robot("Alfred the Coward the Robot", weapon_one)

        self.robots.append(robot_one)
        self.robots.append(robot_two)
        self.robots.append(robot_three)