class Rent(object):
    """
    Rent class. Discounts is a list of all possible discounts to apply to final price.
    That list is extendable with others types of discounts and each discount will
    modify total price of rent.

    Attributes
    ----------
    rent_type : subclasses of BaseRentType
        type of rent
    cuantity : int
        rents count

    Methods
    ----------
    _set_total_price(): sets _total_price attribute
    _apply_discounts(): applies all discounts from _discounts to _total_price
    get_total_price(): set total price, apply discounts to it and return final price

    """
    def __init__(self, rent_type, cuantity):
        self.rent_type = rent_type
        self.cuantity = cuantity
        self._discounts = [FamilyDiscount, ]
        self._total_price = 0

    def _set_total_price(self):
        """Calculates total price of rent and validate entry data"""
        # Validate cuantity data type
        if not isinstance(self.cuantity, int):
            raise TypeError("""Cuantity must be integer""")

        # Validate rent data type
        if not issubclass(self.rent_type, BaseRentType):
            raise TypeError("""Rent type must be subclass of BaseRentType""")

        # calculate total price
        self._total_price = self.cuantity * self.rent_type.price

    def _apply_discounts(self):
        """Apply each discount to total price"""
        for discount in self._discounts:
            discount(self).apply()

    def get_total_price(self):
        """Apply all discounts to total price and return it"""
        self._set_total_price()
        self._apply_discounts()
        return self._total_price


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


class BaseDiscount(object):
    """
    Base class for all discounts.
    Apply method must be implemented for inherited classes

    Methods
    ----------
    __init__(rent): must receive Rent instance
    """
    def __init__(self, rent):
        # rent instance
        self.rent = rent

    def apply(self):
        """Apply discount to total price of rent"""
        raise NotImplementedError("""%s must be implemented""" % __name__)


class FamilyDiscount(BaseDiscount):
    """
    Family discount. Applies if rent count is >= 3 and <= 5.
    """
    def __init__(self, rent):
        super().__init__(rent)

    def apply(self):
        if not isinstance(self.rent, Rent):
            raise TypeError("""Invalid Rent instance""")

        # Discount condition
        if 3 <= self.rent.cuantity <= 5:
            self.rent._total_price = (self.rent._total_price * 70) / 100

