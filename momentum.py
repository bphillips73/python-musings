"""
Program: momentum.py
Author: Brian Phillips

Comput momentum of an object.

Momentum is its mass multiplied by its velocity.
This is a program that accepts an object’s mass
(in kilograms) and velocity (in meters per second)
as inputs and then outputs its momentum.

Inputs: mass      
        velocity 

Output:  momentum        
"""

mass = float(input("Enter the mass in kg: "))
velocity = float(input("Enter the velocity in m/s: "))

momentum = mass * velocity

print("The momentum is " + str(momentum) + " kg m/s")

input("Please press enter or return to quit the program.")





