from .config import initial_city_balance, representative_portion


class City:
    def __init__(self, country, countries_list, x, y):
        self.country = country
        self.x = x
        self.y = y
        self.balance = {x["name"]: 0 for x in countries_list}
        self.balance[country.name] = initial_city_balance
        self.balance_per_day = {x["name"]: 0 for x in countries_list}
        self.neighbours = []
        self.full = False

    def set_neighbours(self, neighbours):
        self.neighbours = neighbours

    def transfer_to_neighbours(self):
        for motif in self.balance:
            balance_of_motif = self.balance[motif]
            amount_to_transfer = balance_of_motif // representative_portion
            if amount_to_transfer > 0:
                for n in self.neighbours:
                    self.balance[motif] -= amount_to_transfer
                    n.add_balance_in_motif(motif, amount_to_transfer)

    def add_balance_in_motif(self, motif: str, amount: int):
        self.balance_per_day[motif] += amount

    def finalize_balance_per_day(self):
        for motif in self.balance_per_day:
            self.balance[motif] += self.balance_per_day[motif]
            self.balance_per_day[motif] = 0

        # check if city is full
        for motif in self.balance_per_day:
            if self.balance[motif] == 0:
                return
        self.full = True
