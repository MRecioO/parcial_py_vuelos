from src.Passenger import Passenger

class Vuelo:
    def __init__(self, desde: str, hasta: str, hora: str, cap: int) -> None:
        self.desde = desde
        self.hasta = hasta
        self.hora = hora
        self.cap = cap
        self.space = cap

        self.passenger: list[Passenger] = []

    #getter
    def get_desde(self) -> str:
        return self.desde
    def get_hasta(self) -> str:
        return self.hasta
    def get_hora(self) -> str:
        return self.hora
    def get_cap(self) -> int:
        return self.cap
    def get_space(self):
        return self.space

    def get_passengers(self) -> list[Passenger]:
        return self.passenger
    #setters
    def set_cap(self, cap) -> None:
        self.cap = cap


    #funs
    def menos_space(self) -> None:
        if self.space > 0:
            self.space -= 1

    def add_passenger(self, passen: Passenger) -> None:
        if passen not in self.passenger:
            self.passenger.append(passen)
            passen.set_donde(self.hasta)

    def list_all_passengers(self, index: int = 0) -> None:
        if index < len(self.passenger):
            print(self.passenger[index])
            self.list_all_passengers(index + 1)

    # Utils
    def __str__(self) -> str:
        return f'Desde: {self.desde}, Hasta: {self.hasta}, Hora: {self.hora}, Asientos libres: {self.space}'

    def __eq__(self, other) -> bool :
        return (self.desde == other.desde and
                self.hasta == other.hasta and
                self.hora == other.hora and
                self.cap == other.cap)





