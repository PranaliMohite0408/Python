class Animal:
    def speak(self):
        print("Anamial Speaking")

#The Childclass Dog inheritance the base
class Dog(Animal):
    def bark(self):
        print("Dog Barking")

#The child class DogChild inherit another child class dog
class DogChild(Dog):
    def eat(self):
        print("Easting bread.....")

d=DogChild()
d.bark()
d.speak()
d.eat()
        
        
