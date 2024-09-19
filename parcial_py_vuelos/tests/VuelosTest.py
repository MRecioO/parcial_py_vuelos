import io
import unittest.mock

from src.Passenger import Passenger
from src.Vuelo import Vuelo


class TestVuelo(unittest.TestCase):

    def setUp(self):
        """Set up the test environment."""
        self.vuelo1 = Vuelo("NLA", "BAS", "09:00", 100)
        self.vuelo2 = Vuelo("BRC", "COR", "10:30", 0)
        self.vuelo3 = Vuelo("NLA", "BAS", "09:00", 100)

        self.passenger1 = Passenger("12345678", "+11 0 11 123255")
        self.passenger2 = Passenger("12345678", "+24 9 100000000")
        self.passenger3 = Passenger("aliennnn", "c j3er nwijnfcd")

    def test_initialization(self):
        """Test the initialization of the Book class."""
        self.assertEqual(self.vuelo1.get_desde(), "NLA")
        self.assertEqual(self.vuelo1.get_hasta(), "BAS")
        self.assertEqual(self.vuelo1.get_hora(), "09:00")
        self.assertEqual(self.vuelo1.get_cap(), 100)

    def test_set_cap(self):
        self.vuelo1.set_cap(100)
        self.assertEqual(self.vuelo1.get_cap(), 100)
        self.vuelo2.set_cap(2)
        self.assertEqual(self.vuelo2.get_cap(), 2)

    def test_menos_space(self):
        self.vuelo1.menos_space()
        self.assertEqual(self.vuelo1.get_space(), 99)

    def test_add_passenger(self):
        self.vuelo1.add_passenger(self.passenger1)
        self.assertEqual(self.vuelo1.get_passengers()[0], self.passenger1)


    def test_eq_method(self):
        """Test the equality comparison of vuelos objects."""
        self.assertEqual(self.vuelo1, self.vuelo3)  # Same ISBN
        self.assertNotEqual(self.vuelo1, self.vuelo2)  # Different ISBN

    def test__str__(self):
        """Test the string representation of the Vuelo object."""
        expected_str = "Desde: NLA, Hasta: BAS, Hora: 09:00, Asientos libres: 100"
        self.assertEqual(str(self.vuelo1), expected_str)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_list_passengers(self, mock_stdout):
        self.vuelo1.add_passenger(self.passenger1)
        self.vuelo1.add_passenger(self.passenger2)
        self.vuelo1.add_passenger(self.passenger3)
        self.vuelo1.list_all_passengers()

        result = mock_stdout.getvalue().splitlines()

        self.assertEqual(result[0], 'DNI: 12345678, Tel: +11 0 11 123255, Destino: BAS')
        self.assertEqual(result[1], 'DNI: 12345678, Tel: +24 9 100000000, Destino: BAS')
        self.assertEqual(result[2], 'DNI: aliennnn, Tel: c j3er nwijnfcd, Destino: BAS')

if __name__ == "__main__":
    unittest.main()
