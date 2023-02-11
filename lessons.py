class Building:
    year = None
    city = None

    def __init__(self, year, city):
        self.year = year
        self.city = city

    def get_info(self):
        print("Year:", self.year, ". City", self.city)


class School(Building):
    pupils = 0

    def __init__(self, pupils,  year, city):
        super(School, self).__init__(year, city)
        self.pupils = pupils

    def get_info(self):
        super().get_info()
        print("Pupils:", self.pupils)


class House(Building):
    residentors = 0

    def __init__(self, residentors, year, city):
        super(House, self).__init__(year, city)
        self.residentors = residentors

    def get_info(self):
            super().get_info()
            print("Residentors:", self.residentors)



class Shop(Building):
    visitors = 0

    def __init__(self, visitors, year, city):
        super(Shop, self).__init__(year, city)
        self.visitors = visitors

    def get_info(self):
            super().get_info()
            print("Visitors:", self.visitors)



school = School(100, 2000, "Kyiv")
school.get_info()
house = House(88, 2000, "Kyiv")
house.get_info()
shop = Shop(200, 2000, "Kyiv")
shop.get_info()