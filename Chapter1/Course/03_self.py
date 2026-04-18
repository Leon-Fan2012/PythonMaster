class Student:
    # Propriétés(attributs) : variables
    name = None
    age = None

    # Comportement : méthodes
    # self est utilisé pour désigner l'objet de la classe lui-même
    def say_hi(self):
        print(f"Bonjour à tous, je m'appelle {self.name} et j'ai {self.age} ans")

    # self est transparent lorsque l'argument est passé et peut être ignoré
    def say_hi2(self, nsg):
        print(f"bonjour à tous, {nsg}.")

# Objet = nom de la classe()
stu1 = Student()
stu1.name = "Alex"
stu1.age = 18
stu1.say_hi()

stu2 = Student()
stu2.name = "Lucie"
stu2.age = 16
stu2.say_hi()
stu2.say_hi2("enchanté de vous rencontrer.")
