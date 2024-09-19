import unittest

from src.Passenger import Passenger


class TestPassenger(unittest.TestCase):

    def setUp(self):
        """Set up the test environment."""
        self.passenger1 = Passenger("12345678", "+11 0 11 123255")
        self.passenger2 = Passenger("12345678", "+24 9 100000000")


    def test_initialization(self):
        """Test the initialization of the Passenger class."""
        self.assertEqual(self.passenger1.get_dni(), "12345678")
        self.assertEqual(self.passenger1.get_tel(), "+11 0 11 123255")
        self.assertEqual(self.passenger2.get_dni(), "12345678")
        self.assertEqual(self.passenger2.get_tel(), "+24 9 100000000")

    def test_set_donde(self):
        self.passenger1.set_donde("BAS")
        self.assertEqual(self.passenger1.get_donde(), "BAS")

    def test__str__(self):
        expected_str = 'DNI: 12345678, Tel: +11 0 11 123255, Destino: '
        self.assertEqual(self.passenger1.__str__(), expected_str)


if __name__ == "__main__":
    unittest.main()
