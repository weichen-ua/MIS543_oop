from car import Car

class Civic(Car):
    def __init__(self, yr = 2016):
        Car.__init__(self,"Honda","Civic")
        self.year = yr

my_civic = Civic()
my_civic.show_model()
print(f"year: {my_civic.year}")

your_civic = Civic()
your_civic.color = "blue"
your_civic.year = 2015
your_civic.show_model()
print("year: %d" % your_civic.year)
print("color: %s" % your_civic.color)