from dinosaur import Dinosaur


class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()


    def create_herd(self):
        dino1 = Dinosaur("Little Foot the dinosaur", 50)
        dino2 = Dinosaur("Blue the Dinosaur", 50)
        dino3 = Dinosaur("Happy the dinosaur", 50)

        self.dinosaurs.append(dino1)
        self.dinosaurs.append(dino2)
        self.dinosaurs.append(dino3)


        