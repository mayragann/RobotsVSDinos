from dinosaur import Dinosaur
from robots import Robot
from fleet import Fleet
from herd import Herd
import random

class Battlefield:
    def __init__(self) -> None:
        self.fleet = Fleet()
        self.herd = Herd()
        
    def run_game(self):
        self.display_welcome()
        self.team = self.choose_team()
        self.battle()


    def display_welcome(self):
        print("Welcome to the brawl of the century!")
        print("Are you ready to rummmmbleeeeee?")
        print("-------------------------------------")
        print("Dinosaurs versus Robots!")
        print("Both Dinosaurs and Robots start with 200 health")
        print("Each contestant begins with 150 stamina")
        print("Attacks will drain each contestant of 10")
        print("There is a fleet of robots and a herd of dinosaurs")
        print("A winner is declared once all Robots in fleet")
        print("or all Dinosaurs in a herd have 0 health")
    def battle(self):
        pass
    def dino_turn(self, dinosaur):
        pass
    def robo_turn(self, robot):
        pass
    def show_dino_opponent_options(self):
        pass
    def show_robo_opponent_options(self):
        pass
    def display_winner(sefl):
        pass