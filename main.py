class Resource:
  def __init__(self,name,amount):
    self.name = name
    self.amount = amount

  def display(self):
    print(f"{self.name}: {self.amount}")
  
power = Resource("Power", 200)
money = Resource("Money", 5000)

power.display()