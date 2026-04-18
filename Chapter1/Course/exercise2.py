class Student:
    name = None
    age = None
    address = None

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

for i in range(1, 6):
    print(f"Actuellemnt en train de saisir le {i}ème élève, 5 élèves au total doivent être saisis")
    name = input("Veuillez saisir le nom de l'élève: ")
    age = input("Veuillez saisir l'âge de l'élève: ")
    address = input("Veuillez saisir l'adresse de l'élève: ")
    stu = Student(name, age, address)
    print(f"La saisie des information sur l'étudiant {i} est complète avec les informations suivantes"
          f" : [ name : {stu.name}, age : {stu.age}, address : {stu.address} ]")
