
class Passenger:
    def __init__(self, dni: str, tel: str, donde: str = "" ) -> None:
        self.__dni = dni
        self.__tel = tel
        self.__donde  = donde

    #getters
    def get_dni(self) -> str:
        return self.__dni
    def get_tel(self) -> str:
        return self.__tel
    def get_donde(self) -> str:
        return self.__donde
    #setters
    def set_donde(self, donde: str) -> None:
        self.__donde = donde


    def __eq__(self, o: object) -> bool:
        if isinstance(o, Passenger):
            return self.__dni == o.get_dni() and self.__tel == o.get_tel() and self.__donde == o.get_donde()
        return False

    def __str__(self) -> str:
        return f"DNI: {self.__dni}, Tel: {self.get_tel()}, Destino: {self.get_donde()}"