class Dog:
    pass

print(type(Dog))

dog_1 = Dog()
dog_2 = Dog()

print(dog_1)
print(dog_2)

print(isinstance(dog_1, Dog))
print(isinstance(dog_2, Dog))
print(type(dog_1))
print(type(dog_2))

dog_1.kind = "Dachshund"
dog_1.life = "12-16 years."
dog_2.kind = "Labrador Retriever"

print(dir(dog_1))