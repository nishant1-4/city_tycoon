from abc import ABC, abstractmethod

class Resource:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def __add__(self, other):
        if not self.name==other.name:
            return False
        return Resource(self.name,self.amount+other.amount)

    def __eq__(self, other):
        return self.amount == other.amount and self.name == other.name
    
    def __str__(self):
        return f"{self.name}: {self.amount}"

    def display(self):
        print(f"{self.name}: {self.amount}")


# power = Resource("Power", 200)
# money = Resource("Money", 5000)

class Building(ABC):
    def __init__(self,name, maintenance_cost):
        self.name = name
        self.maintenance_cost = maintenance_cost

    @abstractmethod
    def produce(self):
        pass
    
    def display(self):
        print(f"Building Name: {self.name}\nMaintenance Cost: {self.maintenance_cost}")
    
class House(Building):
    def __init__(self, name, maintenance_cost,capacity):
        super().__init__(name, maintenance_cost)
        self.capacity = capacity
    
    def produce(self):
        print(f"{self.name} provides upto {self.capacity} citizens")
        return None
    
class Factory(Building):
    def __init__(self, name, maintenance_cost, output_amount):
        super().__init__(name, maintenance_cost)
        self.output_amount = output_amount

    def produce(self):
        return Resource("Money", self.output_amount)
    
    def display(self):
        super().display()
        print(f"Output Amount: {self.output_amount}")

factory = Factory("Steel Factory", 50, 200)
factory.display()
result = factory.produce()
print(result)