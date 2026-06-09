""" base class animal"""

class animal: #blueprint (I want to describe what ALL animals are like)
    
    def __init__(self, name, sound):
        self._name = name               #constructor (When I make an animal, I need a name and a sound)
        self._sound = sound

    def makesound(self):
        print(f"{self._name} makes {self._sound}")

class Dog(animal):
    def __init__(self):
        super().__init__("Dog", "bark")

    def makesound(self):
        print(f"dogs are best")

class Duck(animal):

    def __init__(self):
        super().__init__("Duck","Quack")

    def makesound(self):
        print(f"ducks are better")

class Seal(animal):
    def __init__(self):
        super().__init__("Seal", "screech")

    def makesound(self):
        print(f"seals are okay")

lassy = Dog()

#lassy.makesound()

daffy = Duck()

#daffy.makesound()

salty = Seal()

#salty.makesound()

animals = []

animals.append(lassy)
animals.append(daffy)
animals.append(salty)

for animal in animals:
    animal.makesound()
