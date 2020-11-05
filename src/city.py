from typing import List
from .config import initial_city_balance, representative_portion


class City:
    def __init__(self, country_name: str, countries_list: list, x: int, y: int):
        self.country_name = country_name
        self.x = x
        self.y = y
        self.balance = {c["name"]: 0 for c in countries_list}
        self.balance[country_name] = initial_city_balance
        self.balance_per_day = {c["name"]: 0 for c in countries_list}
        self.neighbours: List['City'] = []
        self.full = False

    def set_neighbours(self, neighbours: List['City']) -> None:
        self.neighbours = neighbours

    def transfer_to_neighbours(self) -> None:
        for motif in self.balance:
            balance_of_motif = self.balance[motif]
            amount_to_transfer = balance_of_motif // representative_portion
            if amount_to_transfer > 0:
                for n in self.neighbours:
                    self.balance[motif] -= amount_to_transfer
                    n.add_balance_in_motif(motif, amount_to_transfer)

    def add_balance_in_motif(self, motif: str, amount: int) -> None:
        self.balance_per_day[motif] += amount

    def finalize_balance_per_day(self) -> None:
        for motif in self.balance_per_day:
            self.balance[motif] += self.balance_per_day[motif]
            self.balance_per_day[motif] = 0

        # check if city is full
        for motif in self.balance_per_day:
            if self.balance[motif] == 0:
                return
        self.full = True
