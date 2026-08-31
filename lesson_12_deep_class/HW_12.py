class Safe:
    def __init__(self, password):
        self.__password = password
        self.__items = []
        self.__limit = 5
        self.__is_locked = True  

    
    def __str__(self):
        status = "locked" if self.__is_locked else "unlocked"
        return f"Safe with {len(self.__items)}/{self.__limit} items ({status})"


    def unlock(self, password):
        if password == self.__password:
            self.__is_locked = False
            print(" Сейф розблоковано.")
        else:
            raise ValueError("Wrong password")

    
    def lock(self):
        self.__is_locked = True
        print(" Сейф заблоковано.")

    
    def __getitem__(self, index):
        
        return self.__items[index]

    def __setitem__(self, index, value):
      
        if self.__is_locked:
            raise PermissionError("Cannot add item: Safe is locked")
        
        
        if len(self.__items) >= self.__limit:
            raise OverflowError("Safe is full (max 5 items)")
        
       
        self.__items.append(value)

   
    def __len__(self):
        return len(self.__items)


    def __contains__(self, item):
        return item in self.__items




my_safe = Safe("Treasure")


print(f"Поточний стан: {my_safe}")
try:
    my_safe.unlock("1234")
except ValueError as e:
    print(f"Помилка: {e}")


try:
    my_safe[0] = "Gold Ring"
except PermissionError as e:
    print(f"Помилка: {e}")


try:
    my_safe.unlock("Treasure")
    my_safe[0] = "Coin"
    my_safe[1] = "Gem"
    my_safe[2] = "Sword"
    my_safe[3] = "Shield"
    my_safe[4] = "Map"
    print(f"Вміст після додавання: {my_safe}")
    
    
    my_safe[5] = "Crown"
except OverflowError as e:
    print(f" Помилка: {e}")
except Exception as e:
    print(f"Непередбачена помилка: {e}")


print(f"Чи є 'Gem' у сейфі? {'Gem' in my_safe}")
print(f"Кількість предметів: {len(my_safe)}")
