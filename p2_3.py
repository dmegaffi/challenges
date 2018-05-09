#tipper



total = float(input("what is the total of your bill?"))

#because I have concantonated "$" and "total" together is must be converted back into a string
print("your bill totals", "$" + str(total))

tip_15 = total * 0.15
tip_20 = total * 0.20

#here I also print a float "tip_var" but no need to convert to string because I did not concantonate
print("A tip of 15% would be", tip_15)
print("A tip of 20% would be", tip_20)
