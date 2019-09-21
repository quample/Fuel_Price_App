
location = input("Enter location: ")
if location == "Texas":
    locationrate = 0.02
else:
    locationrate = 0.04

history = input("Have your ordered here before?: ")
if history == "yes":
    historyrate = 0.01
else:
    historyrate = 0

gallons = int(input("Enter number of gallons: "))
if gallons > 1000:
    gallonsrate = 0.02
else:
    gallonsrate = 0.03

profitfactor = 0.1

month = input("Enter month: ") # case sensative
if month == "March" or month == "April" or month == "May" or month == "June" or month == "July" or month == "August":
    seasonrate = 0.04
else:
    seasonrate = 0.03

#print(locationrate)
#print(historyrate)
#print(gallonsrate)
#print(profitfactor)
#print(seasonrate)

pricepergallon = 1.50 + (locationrate - historyrate + gallonsrate + profitfactor + seasonrate) * 1.50
print("Suggested Price/Gallon: ", pricepergallon)
total = gallons * pricepergallon
print("Total Amount Due: ", total)


