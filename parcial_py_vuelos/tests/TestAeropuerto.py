import io
import unittest.mock

from src.Passenger import Passenger
from src.Vuelo import Vuelo
from src.Aeropuerto import Aeropuerto


class AeropuertoTests(unittest.TestCase):
    def setUp(self):
        self.NLA = Aeropuerto("NLA")
        self.BAS = Aeropuerto("BAS")

        self.passenger1 = Passenger("12345678", "+11 0 11 1232556")
        self.passenger2 = Passenger("12345678", "+24 9 100000000")


        self.vuelo1 = Vuelo("NLA", "BAS", "09:00", 100)
        self.vuelo2 = Vuelo("BRC", "COR", "10:30", 0)


    def test_initialization(self):
        """Test the initialization of the Aeropuerto class."""
        self.assertIsInstance(self.NLA, Aeropuerto)
        self.assertIsInstance(self.BAS, Aeropuerto)
    
    def test_add_vuelo(self):
        self.NLA.add_vuelo(Vuelo("NLA", "BAS", "09:99", 100))
        self.assertEqual(self.NLA.get_vuelos()[0], Vuelo("NLA", "BAS", "09:99", 100))
        
        self.BAS.add_vuelo(Vuelo("BAS", "TUC", "09:99", 123))
        self.assertEqual(self.BAS.get_vuelos()[0],Vuelo("BAS", "TUC", "09:99", 123))



    def test_booking(self):
        #test para que si se haga la reserva
        init_space: int = self.vuelo1.get_space()
        self.assertEqual(init_space, self.vuelo1.get_space())
        self.NLA.booking(self.vuelo1, self.passenger1)
        self.assertEqual(init_space -1, self.vuelo1.get_space())

        self.assertTrue(self.passenger1 in self.vuelo1.get_passengers())

        self.assertEqual(self.vuelo1.get_hasta(), self.passenger1.get_donde())

        #no hay espacio
        init_space: int = self.vuelo2.get_space()
        self.assertEqual(init_space, self.vuelo2.get_space())
        self.NLA.booking(self.vuelo2, self.passenger2)
        self.assertEqual(init_space, self.vuelo2.get_space())

        self.assertTrue(self.passenger2 not in self.vuelo2.get_passengers())

        self.assertEqual('', self.passenger2.get_donde())















