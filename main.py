from nutritionix import NutriConnect
from sheety import SheetyConnection

# Setup Connection Object
nutri_connect = NutriConnect()
sheety_connection = SheetyConnection()

# Get user input
workout = input("What workout did you complete today? ")

# Get nutritional details from workout via API
details = nutri_connect.calc_workout(workout=workout)

# Add workout and nutritional detail to spreadsheet via API
sheety_connection.add_row(details=details)

# records = sheety_connection.get_all_records()
