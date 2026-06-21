# Jaden McKinnon
# 06/21/2026
# P4HW1_VehicleMPG
# This program uses a dictionary to store vehicle MPG values
# and calculates the gallons of gas needed for a trip.

# Create dictionary
vehicles = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

# Store and display keys
keys = vehicles.keys()
print(keys)

# Ask user for vehicle
vehicle = input("\nEnter a vehicle to see its mpg: ")

# Display MPG
print(f"\nThe {vehicle} gets {vehicles[vehicle]} mpg.")

# Ask for miles driven
miles = float(input(f"\nHow many miles will you drive the {vehicle}? "))

# Calculate gallons needed
gallons_needed = miles / vehicles[vehicle]

# Display result
print(f"\n{gallons_needed:.2f} gallon(s) of gas are needed to drive the {vehicle} {miles} miles.")