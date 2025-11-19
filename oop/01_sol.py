class Car :
    __brand = None  #private and encapsulation
    __model = None
    total = 0
    # Constructor
    def __init__(self , brand , model ):   # self this hi he
        self.__brand = brand
        self.__model = model
        Car.total += 1

    def fullname (self):
        print("car name is :",self.__brand , self.__model)

    def get_brand(self):
        return self.__brand
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod    # this is a decorator
    def genral_description():
        return "Cars are means of transport"
    
    @property
    def model(self):
        return self.__model

class ElectricCar(Car) :  #inheritance
    battery_size = None

    def __init__(self, brand, model , battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
      return "Electric Charge"



class Battery:
    def batter_info(self):
        return "this is a battery"


class Engine:
    def engine_info(self):
        return "this is a engine"


class ElectricCarTwo(Battery , Engine ,Car): #Multiple inheritance
    pass


my_new_tesla = ElectricCarTwo("Tesla" ,"Model S")   
print(my_new_tesla.batter_info())
print(my_new_tesla.engine_info())

# tesla_car = ElectricCar('Tesla', 'Model S' , '85KWH' )

# print(isinstance(tesla_car , Car))
# print(isinstance(tesla_car , ElectricCar))


# print(tesla_car.__brand)
# print(tesla_car.get_brand())
# print(tesla_car.fuel_type())


# my_car = Car("Tata" , "Safari")
# my_car.model = 'new model'   # we cant do that beacuse we make read only 
# print(my_car.model())  # we cant do that as well
# print(my_car.model)
# print(my_car.genral_description())  # could not access beacuse we made static method
# print(Car.genral_description())



# my_car = Car("toyota" , "Corolla")
# my_car.fullname()