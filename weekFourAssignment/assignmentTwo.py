class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return f"{self.name} makes a sound."


class Cat(Animal):
    def sound(self):
        return f"{self.name} says: Meow."


class Dog(Animal):
    def sound(self):
        return f"{self.name} says: Bark."


class Cow(Animal):
    def sound(self):
        return f"{self.name} says: Moo."


# Example usage
if __name__ == "__main__":
    animals = [
        Cat("Ronnie"),
        Dog("Rex"),
        Cow("Bessie")
    ]

    for animal in animals:
        print(animal.sound())
