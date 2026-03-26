# Q4 - Age Calculator
# Calculates approximate time conversions from birth year.

import datetime

try:
    year_of_birth = int(input("Enter your birth year: "))
    current_year = datetime.datetime.now().year

    calculated_age = current_year - year_of_birth

    print("\nAge Details")
    print("Age in years:", calculated_age)
    print("Age in months:", calculated_age * 12)
    print("Age in days (approx):", calculated_age * 365)
    print("Years left to reach 100:", 100 - calculated_age)

except:
    print("Enter a valid numeric year.")