"""
Program: nautical.py
Author: Brian Phillips

Convert kilometers to nautical miles.

A program that takes as input a number of kilometers
and prints the corresponding number of nautical miles.

Using the following approximations:
A kilometer represents 1/10,000 of the distance
between the North Pole and the equator.
There are 90 degrees, containing 60 minutes of arc each,
between the North Pole and the equator.
A nautical mile is 1 minute of an arc.

So 90*60 nautical miles = 5400 = 10,000 kilometers,
therefore 1 km = 0.54 nautical miles
1. Significant constants
    CONVERSION_RATE = 0.54
2. The inputs are
       kilometers     
3. Output:  nautical miles

4. Computations: Nautical miles = kilometers x converstion rate

"""
CONVERSION_RATE = 0.54

kilometers = float(input("Enter the distance in kilometers: "))

nauticalMiles = kilometers * CONVERSION_RATE

print(str(kilometers) + " kilometers = " + str(nauticalMiles) + " nautical miles.")

input("Please press enter or return to quit the program.")





