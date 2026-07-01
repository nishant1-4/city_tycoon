from abc import ABC, abstractmethod


class Resource:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def __add__(self, other):
        if not self.name == other.name:
            return False
        return Resource(self.name, self.amount + other.amount)

    def __eq__(self, other):
        return self.amount == other.amount and self.name == other.name

    def __str__(self):
        return f"{self.name}: {self.amount}"

    def display(self):
        print(f"{self.name}: {self.amount}")


# power = Resource("Power", 200)
# money = Resource("Money", 5000)


class Building(ABC):
    def __init__(self, name, maintenance_cost):
        self.name = name
        self.maintenance_cost = maintenance_cost

    @abstractmethod
    def produce(self):
        pass

    def display(self):
        print(f"Building Name: {self.name}\nMaintenance Cost: {self.maintenance_cost}")


class House(Building):
    def __init__(self, name, maintenance_cost, capacity):
        super().__init__(name, maintenance_cost)
        self.capacity = capacity
        self.residents = []

    def produce(self):
        print(f"{self.name} provides upto {self.capacity} citizens")
        return None

    def add_resident(self, citizen):
        if not len(self.residents) < self.capacity:
            print("This house is already full!")
            return
        self.residents.append(citizen)
        print("Citizen added successfully!")

    def list_residents(self):
        if not self.residents:
            print("This house is empty! No one lives here.")
            return
        for count, citizen in enumerate(self.residents):
            print(f"{count+1}. {citizen.name}")


class Factory(Building):
    def __init__(self, name, maintenance_cost, output_amount):
        super().__init__(name, maintenance_cost)
        self.output_amount = output_amount

    def produce(self):
        return Resource("Money", self.output_amount)

    def display(self):
        super().display()
        print(f"Output Amount: {self.output_amount}")


class PowerPlant(Building):
    def __init__(self, name, maintenance_cost, power_output):
        super().__init__(name, maintenance_cost)
        self.power_output = power_output

    def produce(self):
        return Resource("Power", self.power_output)

    def display(self):
        super().display()
        print(f"Power Generated: {self.power_output}")


class Citizen:
    count_id = 1

    def __init__(self, name, savings, happiness):
        self.name = name
        self.savings = savings
        self.happiness = happiness
        self.__citizen_id = Citizen.count_id
        Citizen.count_id += 1

    def get_id(self):
        return self.__citizen_id

    def earn(self, amount):
        if amount <= 0:
            print("Earning should be greater than 0!")
            return
        self.savings += amount

    def pay_tax(self, amount):
        if self.savings < amount:
            print("Not enough savings!")
            return False
        self.savings -= amount
        return True

    def display(self):
        print(
            f"Name: {self.name}\nSavings: {self.savings}\nHappiness: {self.happiness}\nCitizen ID- {self.__citizen_id}"
        )


class City:
    def __init__(self, name, treasury):
        self.name = name
        self.__treasury = Resource("Money", treasury)
        self.buildings = []
        self.citizens = []
        self.tax_dues = []

    def add_building(self, building):
        self.buildings.append(building)
        print(f"{building.name} constructed successfully!")

    def add_citizen(self, citizen):
        self.citizens.append(citizen)
        print("Citizen added successfully")

    def display(self):
        print(f"Name- {self.name}\nTreasury- {self.__treasury.amount}")

    def collect_taxes(self, amount):
        for citizen in self.citizens:
            if citizen.pay_tax(amount):
                self.__treasury.amount += amount
            else:
                self.tax_dues.append(citizen)

