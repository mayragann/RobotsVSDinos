from weapon import  Weapon


class Dinosaur:

    def __init__(self, name, attack_power):
        self.name = name
        self.health = 200
        self.endurance = 150
        self.attack_power = attack_power
        self.weapon_choice = ["Tail whip", "Eyeball scratch", "Firebreath"]
   
    def robot_attack(self, attack_robot):
        if self.endurance > 10:
            while True:
                try:
                    attack_choice = int(input(f'Choose the attack of: (1) {self.weapon_choice [0]} (2) {self.weapon_choice [1]}, or (3) {self.weapon_choice [2]}'))
                except ValueError:
                    continue
                if attack_choice == 1:
                    print(f'{self.name} attacked {attack_robot.name} with {self.weapon_choice [0]}')
                    break
                if attack_choice == 2:
                    print(f'{self.name} attacked {attack_robot.name} with {self.weapon_choice [1]}') 
                    break
                if attack_choice == 3:
                    print(f'{self.name} attacked {attack_robot.name} with {self.weapon_choice [2]}')
                    break
        self.endurance -= 10
        attack_robot.health -= self.weapon.attack_power
        print(f'{self.name} endurance is now {self.endurance}')
        print(f'{attack_robot.name} health is now {attack_robot.health}')