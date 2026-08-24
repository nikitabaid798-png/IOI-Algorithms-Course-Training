# ==================================
# MY HOLIDAY RESERVATION PROGRAM
# ==================================

# PART 1 - DIFFERENT TYPES OF DATA

traveller = "Meera"              # str - stores text
holiday_spot = "Manali"          # str - stores text
cost_per_pass = 850.50           # float - decimal value
pass_count = 3                   # int - whole number
reservation_open = True           # bool - True or False

print("Traveller:", traveller)
print("Holiday Destination:", holiday_spot)
print("Cost of One Ticket: Rs", cost_per_pass)
print("Total Tickets:", pass_count)
print("Reservation Open?", reservation_open)

print(type(traveller))
print(type(holiday_spot))
print(type(cost_per_pass))
print(type(pass_count))
print(type(reservation_open))

# PART 2 - ARITHMETIC OPERATIONS

bill_amount = cost_per_pass * pass_count
offer_amount = 100
payable_amount = bill_amount - offer_amount

print("\nBill Amount: Rs", bill_amount)
print("Offer Discount: Rs", offer_amount)
print("Amount to Pay: Rs", payable_amount)

print("Price of Two Tickets: Rs", cost_per_pass * 2)
print("Price After Rs50 Increase: Rs", cost_per_pass + 50)
print("Price of Half Ticket: Rs", cost_per_pass / 2)

# PART 3 - COMPARISON OPERATIONS

print("\nIs the ticket cost less than Rs1000?", cost_per_pass < 1000)
print("Are more than 2 tickets reserved?", pass_count > 2)
print("Is the holiday spot Manali?", holiday_spot == "Manali")
print("Is the payable amount greater than Rs2000?", payable_amount > 2000)

# PART 4 - STRING OPERATIONS

trip_info = traveller + " has planned a trip to " + holiday_spot + "."
print("\nTrip Information:", trip_info)

print("Destination in capital letters:", holiday_spot.upper())
print("Traveller name in small letters:", traveller.lower())
print("Starting letter of destination:", holiday_spot[0])
print("Number of letters in traveller name:", len(traveller))

# PART 5 - SWAPPING VALUES

early_fare = 700
late_fare = 900

print("\nValues Before Exchange:")
print("Early Fare: Rs", early_fare)
print("Late Fare: Rs", late_fare)

early_fare, late_fare = late_fare, early_fare

print("\nValues After Exchange:")
print("Early Fare: Rs", early_fare)
print("Late Fare: Rs", late_fare)

# FINAL SUMMARY

print("\n================================")
print("HOLIDAY RESERVATION DETAILS")
print("================================")
print("Name:", traveller)
print("Trip Location:", holiday_spot)
print("Number of Passes:", pass_count)
print("Final Payment: Rs", payable_amount)
print("Reservation Status:", reservation_open)
