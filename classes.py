class Dog:
    pass

# print(type(Dog))

dog_1 = Dog()
dog_2 = Dog()

# print(dog_1)
# print(dog_2)

# print(isinstance(dog_1, Dog))
# print(isinstance(dog_2, Dog))
# print(type(dog_1))
# print(type(dog_2))

dog_1.kind = "Dachshund"
dog_1.life = "12-16 years."
dog_2.kind = "Labrador Retriever"

# print(dir(dog_1))
# print(dir(dog_2))

class Dog:
    kind = ""
    age = 0
    name = ""
    vaccinated = False

dog_1.kind = "Golden Retriver"
dog_1.age = 5
dog_1.name = "Fido"
dog_1.vaccinated = True

# print(dog_1.kind, dog_1.age, dog_1.name, dog_1.vaccinated)

dog_2 = Dog()
# print(dog_2.kind, dog_2.age, dog_2.name, dog_2.vaccinated)

dog_2.kind = "Pug"
dog_2.age = 2
dog_2.name = "Suki"
dog_2.vaccinated = True
# print(dog_2.kind, dog_2.age, dog_2.name, dog_2.vaccinated)

class Dog:
    def __init__(self):
        print("Instance initialized")

# dog_1 = Dog()
# dog_2 = Dog()

# class Dog:
#     def __init__():
#         print("Instance initialized")

# dog_1 = Dog()
# dog_2 = Dog()

class Dog:
    def __init__(variable_for_self_can_have_any_name):
        print("Instance initialized")

# dog_1 = Dog()
# dog_2 = Dog()

class Dog:
    def __init__(self, kind, age, name, vaccinated=False):
        self.kind = kind
        self.age = age
        self.name = name
        self.vaccinated = vaccinated

        print("Instance initialized")

dog_1 = Dog("Golden Retriver", 6, "Eric")
dog_2 = Dog("Pub", 4, "Alex", True)

# print(dog_1.__dict__)
# print(dog_2.__dict__)
# print(dog_2.name, dog_2.kind)

class Dog:
    def __init__(self, kind, age, name, vaccinated=False):
        self.kind = kind
        self.age = age
        self.name = name
        self.vaccinated = vaccinated

        print("Instance initialized")
    
    def get_details(self):
        return f"Nmae: {self.name}, Kind: {self.kind}, Age: {self.age}"

dog_1 = Dog("Golden Retriver", 6, "Eric")
dog_2 = Dog("Pub", 4, "Alex", True)

# print(dog_1.get_details())
# print(dog_2.get_details())