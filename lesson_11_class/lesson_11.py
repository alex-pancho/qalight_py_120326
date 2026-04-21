class VeryEasyCar:
    pass

my_first_car = VeryEasyCar()
my_first_car.brand = "Ford"
my_first_car.model = "Cuga"

print(type(my_first_car))
print(isinstance(my_first_car, VeryEasyCar))

print(my_first_car.brand, my_first_car.model)
print("F" in my_first_car.brand)
my_first_car.brand = "Mersedes"
print(my_first_car.brand)

my_second_car = VeryEasyCar()

print(type(my_second_car))
print(isinstance(my_second_car, VeryEasyCar))

# print(my_second_car.brand, my_second_car.model)

class EasyCar:
    
    def __init__(self):
        self.brand = ""
        self.model = ""

my_thrd_car = EasyCar()
my_thrd_car.brand = "Opel"
my_thrd_car.model = "Fusion"
print(my_thrd_car.brand, my_thrd_car.model)

class Car:
    def __init__(self, brand:str, model:str = "TayLaLa"):
        """
        Params: 
            brand:str,
            model:str
        """
        self.brand = brand
        self.model = model
        self.wheels = 4
        self.is_engine_on = False
    
    def __repr__(self):
        return f"Car {self.brand} {self.model} has {self.wheels} wheel"
    
    def change_engine_status(self, passkey=""):
        if passkey == "112233":
            # вкл-викл двигун
            self.is_engine_on = not self.is_engine_on
            print(f"Engine is {"on" if self.is_engine_on else "off"} ")
        else:
            print("Wrong passkey")

my_four_car = Car("BMW", "X5") #
print(my_four_car.brand, my_four_car.model)
print(my_four_car.wheels)

my_car_no5 =  Car("Audi", "Sound")
my_car_no5.wheels = 5
print(my_car_no5.brand, my_car_no5.model)
print(my_car_no5.wheels)
print("Car 5 engine status:", my_car_no5.is_engine_on)
my_car_no5.change_engine_status("112233")
print("Car 5 engine status:", my_car_no5.is_engine_on)
print("Car 4 engine status:", my_four_car.is_engine_on)

print(my_car_no5)

