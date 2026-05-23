class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("Woof woof woof")


class Cat(Animal):
    def speak(self):
        print("Miaou miaou miaou")


def make_noise(animal: Animal):
    animal.speak()


dog = Dog()
cat = Cat()
make_noise(dog)
make_noise(cat)

# Polymorphisme: états multiples
# Lors de l'éxecution dans certain comportement,
# diffèrent objets sont utilisées pour obtenir diffèrents états

# Même comportement, introduction d'objets diffèrents, obtention d'état diffèrents

# classe abstraite: une classe contenant des méthodes abstraites est appelés classe abstraite.
# Méthode abstraite: une méthode dont le corps est une implémeentation vide (pass) est appelée méthode abstraite.
