from typing import List, Tuple, Dict, Set

from src.Passenger import Passenger
from src.Vuelo import Vuelo


class Aeropuerto:
    def __init__(self, ubi: str) -> None:
        self.vuelo: List[Vuelo] = []
        self.ubi: str = ubi
        self.tupu: Tuple[int, str] = (1, "Hello")
        self.dict: Dict[str, int] = {"key": 1}
        self.set: Set[int] = {1, 2, 3}


    # Getters
    def get_vuelos(self) -> List[Vuelo]:
        return self.vuelo
    def get_ubi(self) -> str:
        return self.ubi
    #Sett
    def set_ubi(self, new_ubi: str) -> None:
        self.ubi = new_ubi


    def add_vuelo(self, vuelo: Vuelo) -> None:
        if vuelo.get_desde() == self.ubi:
            self.vuelo.append(vuelo)

    def booking(self, vuelo: Vuelo, passenger: Passenger) -> None:
        if vuelo.get_desde() == self.ubi:
            if vuelo.get_space() > 0:
                vuelo.menos_space()
                vuelo.add_passenger(passenger)