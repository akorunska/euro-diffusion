

class Country:
    def __init__(self, name):
        self.name = name
        self.cities = []
        self.full = False
        self.day_of_full = -1

    def __eq__(self, other):
        return self.day_of_full == other.day_of_full

    def __lt__(self, other):
        return self.day_of_full < other.day_of_full

    def append_city(self, city):
        self.cities.append(city)

    def check_fullness(self, day):
        if self.full:
            return
        for city in self.cities:
            if city.full is False:
                return
        self.full = True
        self.day_of_full = day

    def has_foreign_neighbours(self):
        has_foreign_neighbours = False
        for c in self.cities:
            for n in c.neighbours:
                if n.country.name != self.name:
                    has_foreign_neighbours = True
        return has_foreign_neighbours

    def only_county_mode(self):
        self.full = True
        self.day_of_full = 1