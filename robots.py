class Robot:
    def __init__(self, name, Weapon):
        self.name = name
        self.health = 100
        self.weapon = Weapon
        self.weapon_choice = ['Lazer Beam', 'Gravity Gun', 'lightning']


    def attack_dinosaur(self, dinosaur_to_attack):
        if self.health > 10:
            while True:
                try:
                    attack_choice = int(input(f'Choose attack type: (1) {self.weapon_choice[0]}, (2) {self.weapon_choice[1]}, or (3) {self.weapon_choice[2]}.: '))
                except ValueError:
                    continue
                if attack_choice == 1:
                    print(f'{self.name} attacked {dinosaur_to_attack.name} with {self.weapon_choice[0]}')
                    break
                elif attack_choice == 2:
                    print(f'{self.name} attacked {dinosaur_to_attack.name} with {self.weapon_choice[1]}')
                    break
                elif attack_choice == 3:
                    print(f'{self.name} attacked {dinosaur_to_attack.name} with {self.weapon_choice[2]}')
                    break

           
            dinosaur_to_attack.health -= self.weapon.attack_power
            print(f'{dinosaur_to_attack.name} health is now {dinosaur_to_attack.health}')