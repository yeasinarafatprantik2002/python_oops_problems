class Car:
    total_cars = 0

    def __init__(self, brand="brand", model="model"):
        self.__brand = brand
        self.__model = model
        self.total_cars += 1

    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand = brand

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

    def full_name(self):
        return f"{self.__brand} {self.__model}"

    def fuel_type(self):
        return "Petrol or Diesel"

    @staticmethod
    def general_description():
        return f"Cars are means of transportation"

    @property
    def model(self):
        return self.__model


class ElectricCar(Car):
    def __init__(
        self,
        brand,
        model,
        battery_size,
    ):
        self.battery_size = battery_size
        super().__init__(brand, model)

    def fuel_type(self):
        return "Electricity"


my_car = Car()
my_car.set_brand("Toyota")
my_car.set_model("Corolla")
# my_car.model = "Coroll"
# print(my_car.full_name())
# print(my_car.get_brand())
# print(my_car.fuel_type())
# print(Car().total_cars)
# print(my_car.general_description())
# print(Car().general_description())
# print(my_car.model)


# my_electric_car = ElectricCar("Tesla", "Model S", 100)
# print(my_electric_car.full_name())
# print(my_electric_car.fuel_type())
# print(my_electric_car.battery_size)

# my_electric_car = ElectricCar("Tesla", "Model S", 100)
# print(isinstance(my_electric_car, ElectricCar))
# print(isinstance(my_electric_car, Car))


class Battery:
    def battery_info(self):
        return "This is a battery"


class Engine:
    def engine_info(self):
        return "This is an engine"


class ElectricCarTwo(Battery, Engine, Car):
    pass


new_tesla = ElectricCarTwo("Tesla", "Model S")

print(new_tesla.battery_info())
print(new_tesla.engine_info())
