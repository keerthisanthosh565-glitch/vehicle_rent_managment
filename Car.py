from Vehicle import Vehicle  # import vehicle 
class Car(Vehicle):
    def calculate_rent(self,day):  # inherit from employee class
        self.day = day
        total_rent =self.rental_price * self.day+500
        print("total_rent:",total_rent)
        return total_rent

    
    def display_vehicle_details(self):  #display details
        print("name:",self.name)
        print("rental_price:",self.rental_price)
        

