'''Task 1
Calculate a user's total holiday costs.
Collect city they are flying to, number of nights, number of car hire days.
Create functions to calculate the costs associated.
Print out the relevant details in a readable logical format.
'''

# Setting the required variables
flights = {"paris": 150, "madrid": 159, "prague": 260, "sydney": 998}
hotels_per_night = {"paris": 99, "madrid": 89, "prague": 67, "sydney": 109}
daily_car_cost = {"paris": 65, "madrid": 58, "prague": 45, "sydney": 65}
city_flight = "0"
flight_price = 0
car_hire_daily = 0
rental_days = 0
num_nights = 0
hotel_daily_cost = 0

# Show available cities
print("\nWelcome to Holi-bot")
print("\nWe will calculate your holiday costs together.")
print("\nThe available cities are as follows:-")
for key in flights:
    print("   " + key.title())

# Gather the city the user plans to travel to, if unknown give error to try again (hence the loop)
while city_flight == "0":
    city_flight = input(str("\nAll flights depart from London Heathrow.\nAll flights are return.\nPlease first enter the name of the city you are flying to: "))
    city_flight = city_flight.lower()
    if city_flight == "paris":
        city_flight = city_flight.title()
        print(f"City: {city_flight}")
    elif city_flight == "madrid":
        city_flight = city_flight.title()
        print(f"City: {city_flight}")
    elif city_flight == "prague":
        city_flight = city_flight.title()
        print(f"City: {city_flight}") 
    elif city_flight == "sydney":
        city_flight = city_flight.title()
        print(f"City: {city_flight}")
    else:
        print("\nOops, that's not a selectable city. Please check your spelling and try again.")
        print("\nThe available cities are as follows:-")
        for key in flights:
            print("   " + key.title())
        city_flight = "0"

# make city_flight lowwer case so as to be usable with the dictionaries.
city_flight = city_flight.lower()

# get flight price from dictionary
for key, value in flights.items():
    if city_flight == key:
        flight_price = value
        print(f"Flight Price: £{flight_price}")

# Get daily hotel cost from dictionary
for key, value in hotels_per_night.items():
    if city_flight == key:
        hotel_daily_cost = value
print(f"Hotel cost per day: £{hotel_daily_cost}")

# Get daily car cost from dictionary
for key, value in daily_car_cost.items():
    if city_flight == key:
        car_hire_daily = value
print(f"Car hire cost per day: £{car_hire_daily}")

# Collect the number of nights and number of car rental days from user.
# Check input is only integers and re-ask if not. Then convert to integer (this avoids an error out on incompatible input).
# Re-ask for rental days if more rental days than holiday length.
num_nights = input("\nHow many days will you be staying: ")
while num_nights.isdigit() == False:
    print("Error, please only type integers (not text or special characters)")
    num_nights = input("\nHow many days will you be staying: ")
num_nights = int(num_nights)

rental_days = input("\nHow many days will you be renting a car for: ")
while rental_days.isdigit() == False:
    print("Error, please only type integers (not text or special characters)")
    rental_days = input("\nHow many days will you be renting a car for: ")
rental_days = int(rental_days)

while rental_days>num_nights:
    print("Your car rental days are more than your stay.")
    rental_days = int(input("Please confirm the number of car rental days: "))
    if rental_days > num_nights:
        car_uncertainty = input(f"You have selected {rental_days} car rental days when your holiday is {num_nights} days, is this correct? Y/N: ")
        car_uncertainty = car_uncertainty.lower()
        if car_uncertainty == "y":
            break

# Function to find total hotel costs
def hotel_cost(a, b):
    total = a * b
    return (float(round(total,2)))
hotel_total = hotel_cost(num_nights, hotel_daily_cost)
print(f"\nTotal hotel cost: £{hotel_total}")

# Function to find total flight costs
def plane_cost(a, b):
    b = (a/100)*10
    total = a + b
    return (float(round(total,2)))
flights_total = plane_cost(flight_price,0)
print(f"Total flight costs (plus 10% admin fees): £{flights_total}")

# Function to find total car hire costs
def car_rental(a,b):
    total = a * b
    return (float(round(total,2)))
car_total = car_rental(rental_days, car_hire_daily)
print(f"Total car hire cost: £{car_total}")

# Function to find full holiday cost
def holiday_cost(plane,car,hotel):
    total = plane + car + hotel
    return (float(round(total,2)))
total_cost = holiday_cost(flights_total,car_total,hotel_total)
print(f"\nYour total holiday price is: £{total_cost}")