from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self) -> str:
        pass

class Dog(Animal):
    def sound(self) -> str:
        return "Woof!"

class Cat(Animal):
    def sound(self) -> str:
        return "Meow!"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type: str) -> Animal:
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")

if __name__ == "__main__":
    factory = AnimalFactory()
    dog = factory.create_animal("dog")
    cat = factory.create_animal("cat")
    
    print(dog.sound())
    print(cat.sound())
