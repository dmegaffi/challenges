#Car salesman challenge
#the input is a string, so must be converted to an int for the tax_base formula to work

base = int(input("what is the base price of your car?"))
delivery = 50
car_prep = 100
tax_base = base + delivery + car_prep
tax_expense = float(tax_base) * 0.15
total = tax_base + tax_expense

print("thank you for purchasing your car from us!")
print("the base price is", base)
input("correct?")
print("after delivery, car prep, and taxes your new car comes to", total)
