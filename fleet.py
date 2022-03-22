from robots import Robot
from weapon import Weapon


class Fleet:
    def __init__(self):
        self.robots = []
        self.create_fleet()


    def create_fleet(self):
        weapon1 = Weapon("Burning Sword", 50)
        weapon2 = Weapon("Sword Gun", 50)
        weapon3 = Weapon("Rocket Launcher", 50)

        robot1 = Robot("Tinkerbell the Robot", weapon1)
        robot2 = Robot("Charming the Robot", weapon2)
        robot3 = Robot("Alfred the Coward the Robot", weapon3)

        self.robots.append(robot1)
        self.robots.append(robot2)
        self.robots.append(robot3)