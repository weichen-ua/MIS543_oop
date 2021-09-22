class Car(object):
    def __init__(self, br = "abstract car", md = "unknown"):
        self.brand = br
        self.model = md
        self.mileage = 0

    def add_mileage(self, miles):
        self.mileage += miles
        print(self.mileage)

    def show_model(self):
        print("Brand: " + self.brand)
        print("Model: " + self.model)

my_car = Car("Honda", "Civic")
my_car.show_model()

