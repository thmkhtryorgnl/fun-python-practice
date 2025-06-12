#!/usr/bin/python3
#This example for Abstarct Class:
from abc import ABC,abstractmethod
class Animal(ABC): #use ABC for use class for abstract
    @abstractmethod #convert function to abstract
    def sound(self):
        pass
class Duck(Animal):
    def sound(self):
        return "quack quack"
class Cow(Animal):
    def sound(self):
        return "Maaaa Ma"
c = Cow()
print (c.sound())