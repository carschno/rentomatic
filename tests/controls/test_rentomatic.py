import unittest

from rentomatic.controls.rentomatic import Rentomatic, UnavailableError
from rentomatic.models.transport import Car


class RentomaticTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.rentomatic = Rentomatic()

    def test_list(self):
        car = Car()
        self.rentomatic.add_transport(car)
        transports = self.rentomatic.transports
        self.assertEqual([car], transports)

    def test_list_empty(self):
        transports = self.rentomatic.transports
        self.assertEqual([], transports)

    def test_list_avail(self):
        car = Car()
        self.rentomatic.add_transport(car)
        transports = self.rentomatic.available_transports()
        self.assertEqual([car], transports)

    def test_list_avail_none(self):
        car = Car()
        car.available = False
        self.rentomatic.add_transport(car)
        transports = self.rentomatic.available_transports()
        self.assertEqual([], transports)

    def test_list_avail_name(self):
        car = Car()
        self.rentomatic.add_transport(car)
        transports = self.rentomatic.available_transport_name("Car")
        self.assertEqual([car], transports)

    def test_list_avail_name_none(self):
        car = Car()
        self.rentomatic.add_transport(car)
        transports = self.rentomatic.available_transport_name("Bike")
        self.assertEqual([], transports)

    def test_get_by_id(self):
        car = Car()
        self.rentomatic.add_transport(car)
        transport = self.rentomatic.get_by_id(car.id)
        self.assertEqual(car, transport)

    def test_get_by_id_invalid(self):
        with self.assertRaises(ValueError):
            self.rentomatic.get_by_id(-1)

    def test_rent(self):
        car = Car()
        self.rentomatic.add_transport(car)
        rented = self.rentomatic.rent(car.id)
        self.assertEqual(car, rented)
        self.assertFalse(car.available)

    def test_rent_bad_id(self):
        with self.assertRaises(ValueError):
            self.rentomatic.rent(-1)

    def test_rent_unavailable(self):
        car = Car()
        car.available = False
        self.rentomatic.add_transport(car)

        with self.assertRaises(UnavailableError):
            self.rentomatic.rent(car.id)

    def test_return(self):
        car = Car()
        self.rentomatic.add_transport(car)
        self.rentomatic.rent(car.id)
        self.rentomatic.return_transport(car)
        self.assertTrue(car.available)


if __name__ == '__main__':
    unittest.main()
