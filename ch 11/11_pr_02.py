class Animals:
    animalType="Mammal"

class Pets(Animals):
    color="white"

class dog(Pets):
    @staticmethod
    def bark():
        print("BOw BoW!")
    
d=dog()
d.bark()
print(d.color)