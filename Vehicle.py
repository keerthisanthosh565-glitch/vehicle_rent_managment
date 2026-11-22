from abc import ABC, abstractmethod
class Vehicle(ABC):     # import into abstract metod
    @abstractmethod
    def calculate_rent(day):
        pass
    def display_vehicle_details(self):  # display vehicle details
        pass

    def __init__(self,name,rental_price):  # initalizes vehicle detaails
        self.name = name
        self.__rental_price = rental_price

    @property
    def rental_price(self):      # rental price private attribute
        return self.__rental_price
        

        


