# Creates objects without exposing creation logic.


class Dog:
    def speak(self):
        return "Woof!"


class Cat:
    def speak(self):
        return "Meow!"


class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        if animal_type == "cat":
            return Cat()
        raise ValueError("Unknown animal type")


if __name__ == "__main__":
    pet = AnimalFactory.create_animal("dog")
    print(pet.speak())
