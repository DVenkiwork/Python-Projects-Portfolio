# vehicle_system.py
# Objective: This is a simple project to implement basic Class, subclass, inheritance, and Polymorphism concepts.
# This code demonstrates how different vehicle types can share common characteristics while exhibiting unique behaviors.
# ###################################################################################


class Vehicle:
    """
    Represents a generic vehicle.
    """
    def __init__(self, make, model):
        """
        Initializes a Vehicle with a make and model.

        Args:
            make (str): The manufacturer of the vehicle.
            model (str): The specific model of the vehicle.
        """
        self.make = make
        self.model = model
        
    def display_info(self):
        """
        Displays general information about the vehicle.
        """
        print(f"Vehicle: {self.make} {self.model}")
        
class Car(Vehicle):
    """
    Represents a car, inheriting from Vehicle.
    """
    def __init__(self, make, model, num_doors):
        """
        Initializes a Car with make, model, and number of doors.

        Args:
            make (str): The manufacturer of the car.
            model (str): The specific model of the car.
            num_doors (int): The number of doors the car has.
        """
        super().__init__(make, model) # Call the parent class's __init__
        self.num_doors = num_doors # Add a car-specific attribute
        
    def display_info(self):
        """
        Overrides the display_info method to show car-specific details.
        """
        super().display_info() # Call the parent's display_info for common info
        print(f"Type: Car | Doors: {self.num_doors}")
        
class Motor_bike(Vehicle):
    """
    Represents a motorbike, inheriting from Vehicle.
    """
    def __init__(self, make, model, engine_cc):
        """
        Initializes a Motor_bike with make, model, and engine CC.

        Args:
            make (str): The manufacturer of the motorbike.
            model (str): The specific model of the motorbike.
            engine_cc (int): The engine displacement in cubic centimeters.
        """
        super().__init__(make, model) # Call the parent class's __init__
        self.engine_cc = engine_cc # Add a motorbike-specific attribute
        
    def display_info(self):
        """
        Overrides the display_info method to show motorbike-specific details.
        """
        super().display_info() # Call the parent's display_info for common info
        print(f"Type: Motorbike | Engine: {self.engine_cc}cc")
        

if __name__ == "__main__":
    print("--- Demonstrating Vehicle System ---")
    
    # Creating instances of subclasses
    honda_car = Car("Honda", "CRV", 5)
    toyota_car = Car("Toyota", "Camry", 4)
    lamborgini_car = Car("Lamborgini", "Urus", 2)
    
    harley_bike = Motor_bike("Harley Davidson", "Fat Bob", 1868)
    yamaha_bike = Motor_bike("Yamaha", "YZF-R1", 998)
    
    # Storing different vehicle objects in a list
    vehicles_in_showroom = [honda_car, toyota_car, lamborgini_car, harley_bike, yamaha_bike]
    
    print("\n--- Displaying Info for Various Vehicles ---")
    # Iterating through the list and calling display_info() on each object
    # This demonstrates polymorphism: the same method call behaves differently
    # based on the object's actual type.
    for vehicle in vehicles_in_showroom:
        vehicle.display_info()
        print("-" * 20) # Separator for readability

    print("\n--- End of Demonstration ---")
