
from weapon import Weapon


class Robot:    
    def __init__(self, name):
        self.name = name
        self.health = 200
        self.endurance = 150
        self.weapon = Weapon
        self.weapon_choice = ["Bazooka", "Lazer Gun", "Fists of Death"]
        
        

    def robot_attack(self, dinosaur_to_destroy):
        if self.endurance > 10:
            while True:
                try:
                    attack_choice = int(input(f"Choose attack: (1) {self.weapon_choice [0]}, (2) {self.weapon_choice [0]}"))
                except ValueError:
                    continue
                if attack_choice == 1:
                    print(f'{self.name} attacked {dinosaur_to_destroy.type} with {self.weapon_choice[0]}')
                    break
                elif attack_choice == 2:
                    print(f'{self.name} attacked {dinosaur_to_destroy.type} with {self.weapon_choice[1]}')
                    break
                elif attack_choice == 3:
                    print(f'{self.name} attacked {dinosaur_to_destroy.type} with {self.weapon_choice[2]}')
                    break
        self.endurance -= 10
        dinosaur_to_destroy.health -= self.weapon.attack_power
        print(f'{self.name} endurance is now {self.endurance}')
        print(f'{dinosaur_to_destroy.type} health is now {dinosaur_to_destroy.health}')



   
