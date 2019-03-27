class Rent(object):
    """
    Attributes
    ----------
    rent_type : subclasses of BaseRentType
        type of rent
    cuantity : int
        rents count

    Methods
    ----------
    get_total_price(): calculate and get total rent price
    """
    def __init__(self, rent_type, cuantity):
        self.rent_type = rent_type
        self.cuantity = cuantity

    def _validate_input_data(self):
        # Validate cuantity data type
        if not isinstance(self.cuantity, int):
            raise TypeError("""Cuantity must be integer""")

        # Validate rent data type
        if not issubclass(self.rent_type, BaseRentType):
            raise TypeError("""Rent type must be subclass of BaseRentType""")

    def get_total_price(self):
        """Calculate total price. Validate input"""
        self._validate_input_data()
        return float(self.rent_type.price * self.cuantity)


class FamilyRent(object):
    """
    Attributes
    ----------
    rentals : subclasses of Rent
        rentals

    Methods
    ----------
    get_total_price(): calculate and get total price of rentals with discount
    """
    def __init__(self, *rentals):
        self.rentals = rentals

    def _validate_input_data(self):
        # Validate type
        for rent in self.rentals:
            if not isinstance(rent, Rent):
                raise TypeError("""All rentals must be Rent instance""")
        # Validate rentals count
        if not 3 <= len(self.rentals) <= 5:
            raise ValueError("""The amount of rentals should be from 3 to 5""")

    def get_total_price(self):
        """Get total price of rentals with discount"""
        self._validate_input_data()

        total_price = 0
        for rent in self.rentals:
            total_price += rent.get_total_price()

        return float((total_price * 70) / 100)


class BaseRentType(object):
    """
    Base class of rent type. Cannot be used.
    """
    price = 0


class RentByHour(BaseRentType):
    """Rent by hour"""
    price = 5


class RentByDay(BaseRentType):
    """Rent by day"""
    price = 20


class RentByWeek(BaseRentType):
    """Rent by week"""
    price = 60
