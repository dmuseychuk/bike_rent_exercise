from lib import Rent, FamilyRent, RentByDay, RentByHour, RentByWeek

# 2 hour rents
rent_1 = Rent(RentByHour, 2)
print("%s" % '-'*20)
print("2 hour rents price: $%s" % rent_1.get_total_price())
print("%s" % '-'*20)

# 5 week rents
rent_2 = Rent(RentByWeek, 5)
print("%s" % '-'*20)
print("5 week rents price: $%s" % rent_2.get_total_price())
print("%s" % '-'*20)

# 7 day rents
rent_3 = Rent(RentByDay, 7)
print("%s" % '-'*20)
print("7 day rents price: $%s" % rent_3.get_total_price())
print("%s" % '-'*20)

# Family rent. 3 previous rents objects used
family_rent = FamilyRent(rent_1, rent_2, rent_3)
print("%s" % '-'*20)
print("Family rent: $%s" % family_rent.get_total_price())
print("%s" % '-'*20)
