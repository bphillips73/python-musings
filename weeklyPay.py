"""
Program: weeklyPay.py
Author: Eric (Brian) Phillips

Compute a person's weekly pay with overtime

1. Significant constants
    OVERTIME_RATE = 1.5
2. The inputs are
       hourlyWage
       regularHours
       overtimeHours
       
3. Computations:
       regularPay = hourlyWage * regularHours
       overtimePay = overtimeHours * OVERTIME_RATE * hourlyWage
       weeklyPay = overtimePay + regularPay

4. The outputs are
       the total weekly pay
"""

# Initialize the constants
OVERTIME_RATE = 1.5

# Request the inputs
hourlyWage = float(input("Enter the hourly wage: "))
regularHours = float(input("Enter the number of regular hours worked: "))
overtimeHours = float(input("Enter the number of ovetime hours worked: "))

# Compute the total weekly pay
regularPay = hourlyWage * regularHours
overtimePay = overtimeHours * OVERTIME_RATE * hourlyWage
weeklyPay = round(overtimePay + regularPay, 2)
         
# Display the weekly pay
print("The total pay is $" + str(weeklyPay))
