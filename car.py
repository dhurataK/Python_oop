class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = 0.12
    def display_all(self):
        if self.price > 10000:
            self.tax = 0.15
        print " Price: {}\n Speed: {}\n Fuel: {}\n Mileage: {}\n Tax: {}\n".format(self.price, self.speed, self.fuel, self.mileage,self.tax)
#Creating instances of class Car
car1 = Car(2000,"35mph","Full","15mpg")
car1.display_all()

car2 = Car(2000,"5mph","Not Full","105mpg")
car2.display_all()

car3 = Car(2000,"15mph","Kind of Full","95mpg")
car3.display_all()

car4 = Car(2000,"25mph","Full","25mpg")
car4.display_all()

car5 = Car(2000,"45mph","Empty","25mpg")
car5.display_all()

car6 = Car(20000000,"35mph","Empty","15mpg")
car6.display_all()
