from unittest import TestCase, main
from lib import Rent, RentByWeek, RentByHour, RentByDay, BaseRentType, FamilyRent


class TestRent(TestCase):
    """Test Rent class. Test all possible rent types and exceptions"""
    def test_invalid_rent_type_exc(self):
        rent = Rent(1, 1)
        self.assertRaises(TypeError, rent.get_total_price)

    def test_invalid_rent_cuantity_exc(self):
        rent = Rent(RentByDay, 1.1)
        self.assertRaises(TypeError, rent.get_total_price)

    def test_week_rent_price(self):
        rent = Rent(RentByWeek, 1)
        self.assertEqual(rent.get_total_price(), RentByWeek.price)

    def test_day_rent_price(self):
        rent = Rent(RentByDay, 1)
        self.assertEqual(rent.get_total_price(), RentByDay.price)

    def test_hour_rent_price(self):
        rent = Rent(RentByHour, 1)
        self.assertEqual(rent.get_total_price(), RentByHour.price)

    def test_base_rent_type_used(self):
        rent = Rent(BaseRentType, 100)
        self.assertEqual(rent.get_total_price(), 0)


class TestFamilyRent(TestCase):
    """Test family rent class"""
    def setUp(self):
        # set initial data
        self.rentals = [
            Rent(RentByWeek, 1),
            Rent(RentByHour, 1),
            Rent(RentByDay, 1)
        ]

    def test_family_rent_price(self):
        # Test valid rentals price
        family_rent = FamilyRent(*self.rentals)
        rentals_price = (sum([rent.rent_type.price for rent in self.rentals]) * 70) / 100
        self.assertEqual(rentals_price, family_rent.get_total_price())

    def test_rentals_type_exc(self):
        # Validate throwed exception for rentals type
        rentals_with_invalid_rental = self.rentals + ['invalid_rental']
        family_rent = FamilyRent(*rentals_with_invalid_rental)
        self.assertRaises(TypeError, family_rent.get_total_price)

    def test_rentals_count_exc(self):
        # Validate throwed exception for rentals count
        family_rent_with_6_rents = FamilyRent(*(self.rentals * 2))
        family_rent_with_0_rents = FamilyRent(*[])
        self.assertRaises(ValueError, family_rent_with_6_rents.get_total_price)
        self.assertRaises(ValueError, family_rent_with_0_rents.get_total_price)


if __name__ == '__main__':
    main()
