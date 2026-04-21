
# наслідування
class Animal:

    def birth(self):
        print("this animal has births")

    def speak(self):
        pass

class Dog(Animal):
    # поліморфізм 
    def speak(self):
        return "Wof!"

    def seek(self):
        return "I'm looking for a toy"

class Cat(Animal):
    # поліморфізм
    def speak(self):
        return "Meew!"

    def sleep(self):
        return "I'm sleeping now"

class Koza(Animal):
    # поліморфізм
    def speak(self):
        return "Meee"


patron = Dog()
murzik = Cat()
belka = Koza ()

print(patron.seek())
print(murzik.sleep())
patron.birth()
murzik.birth()

# поліморфізм
print(patron.speak())
print(murzik.speak())
print(belka.speak())

# інкапсуляція

class BankAccount:

    def __init__(self, initial_balance):
        self.__balance = initial_balance
    
    def __repr__(self):
        return f"Available: {self.__balance} USD"
    
    def get_balance(self):
        return self.__balance

    def set_balance(self, value):
        if isinstance(value, (int, float)):
            self.__balance = value
    
    
account = BankAccount(1000)
print(account)
account.set_balance(100)
print(account.get_balance())
print(account)

alex = BankAccount(10)
nata = BankAccount(25)
alex_bal = alex.get_balance()
print( alex_bal > nata.get_balance())

# Без ООП
a_name = "John"
a_age = 25
print(f"{a_name} is {a_age} years old.")

b_name = "Alex"
b_age = 47
print(f"{b_name} is {b_age} years old.")

# З ООП
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"{self.name} is {self.age} years old."

person1 = Person("Jon", 15)
person2 = Person("Daeneris", 15)
person3 = Person("Tyrion", 30)
person4 = Person("Sansa", 15)
person5 = Person("Arya", 10)
person6 = Person("Jaime", 35)
person7 = Person("Cersei", 35)

print(person1.get_info())
print(person2.get_info())
print(person3.get_info())
print(person4.get_info())
print(person5.get_info())
print(person6.get_info())
print(person7.get_info())

class Vehicle:
    def __init__(self, color):
        self.color = color

class NewCar(Vehicle):
    def __init__(self, color, brand):
        super().__init__(color)
        # self.color = Vehicle(color)
        self.brand = brand

my_new_car = NewCar("white", "Dodge")
print(my_new_car.color, my_new_car.brand)

class Employee(Person):

    def __init__(self, name, age, job_title):
        super().__init__(name, age)
        self.job_title = job_title

    def __repr__(self):
        return f"{self.name} is {self.age} years old and work as {self.job_title}"


new_human = Employee("Kira", 27, "CEO")

print(new_human)
print(new_human.get_info())