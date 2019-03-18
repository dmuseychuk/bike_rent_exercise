from unittest import TestCase, main
from lib import Rent, RentByWeek, RentByHour, RentByDay, BaseRentType, FamilyDiscount


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


class TestDiscount(TestCase):
    """Test all discount classes"""
    def test_family_discount(self):
        # Apply only family discount to total price of rent
        rent = Rent(RentByHour, 5)
        rent._set_total_price()
        FamilyDiscount(rent).apply()
        self.assertEqual(rent._total_price, 17.5)

    def test_family_discount_type_exc(self):
        # Apply only family discount to total price of rent
        discount = FamilyDiscount(1)
        self.assertRaises(TypeError, discount.apply)

    def test_family_discount_without_discount_condition(self):
        # Apply only family discount to total price of rent,
        # the result will be same as without discount
        rent = Rent(RentByHour, 2)
        rent._set_total_price()
        FamilyDiscount(rent).apply()
        self.assertEqual(rent._total_price, 10)


if __name__ == '__main__':
    main()
