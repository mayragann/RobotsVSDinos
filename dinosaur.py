class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.health = 100
        self.attack_power = attack_power
        self.attack_type = ('Eyeball Scratch', 'Lava Bite', 'Deep Slash')


    def attack_robot(self, robot_to_attack):
        if self.health > 10:
            while True:
                try:
                    attack_choice = int(input(f'Choose attack type: (1) {self.attack_type[0]}, (2) {self.attack_type[1]}, or (3) {self.attack_type[2]}.: '))
                except ValueError:
                    continue
                if attack_choice == 1:
                    print(f'{self.name} attacked {robot_to_attack.name} with {self.attack_type[0]}')
                    break
                elif attack_choice == 2:
                    print(f'{self.name} attacked {robot_to_attack.name} with {self.attack_type[1]}')
                    break
                elif attack_choice == 3:
                    print(f'{self.name} attacked {robot_to_attack.name} with {self.attack_type[2]}')
                    break

            
            robot_to_attack.health -= self.attack_power
            print(f'{robot_to_attack.name} health is now {robot_to_attack.health}')
