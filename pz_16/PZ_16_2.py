#Создайте класс "Животное", который содержит информацию о виде и возрасте животного. Создайте классы "Собака" и "Кошка", которые наследуются от класса
# "Животное" и содержат информацию о породе.

class Animal:
    def __init__(self, species, age):
        self.species = species
        self.age = age

class Dog(Animal):
    def __init__(self, species, age, breed):
        super().__init__(species, age)
        self.breed = breed

class Cat(Animal):
    def __init__(self, species, age, breed):
        super().__init__(species, age)
        self.breed = breed

dog = Dog("Собака", 3, "Золотистый ретривер")
cat = Cat("Кошка", 5, "Британская веслоухая")

print("Вид животного:", dog.species)
print("Возраст собаки:", dog.age)
print("Порода собаки:", dog.breed)

print("Вид животного:", cat.species)
print("Возраст кошки:", cat.age)
print("Порода кошки:", cat.breed)