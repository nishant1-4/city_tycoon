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


power = Resource("Power", 200)
money = Resource("Money", 5000)
power2 = Resource("Power",300)

power3 = power+power2
print(power3)
print(power)