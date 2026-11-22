from Vehicle import Vehicle   # import vehicle 

class Bike(Vehicle):     # inherita
    def calculate_rent(self,day):  # override the vehicle  calculation rent
        self.day = day
        total_rent =(self.rental_price * self.day)+100
        print("total_rent:",total_rent)
        return total_rent

    def display_vehicle_details(self): # display details 
        print("name:",self.name)
        print("rental_price:",self.rental_price)
        