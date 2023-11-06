class Glass:
    def __init__(self, capacity, amount=0):
        self.capacity = capacity
        self.amount = amount

    def pour_in(self, amount):
        self.amount += amount
        if self.amount > self.capacity:
            self.amount = self.capacity

    def pour_out(self, amount):
        self.amount -= amount
        if self.amount < 0:
            self.amount = 0


bottle = Glass(100)
print(bottle.amount)

bottle.pour_out(50)
print(bottle.amount)

bottle.pour_out(51)
print(bottle.amount)
