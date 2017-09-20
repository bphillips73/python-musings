"""
Program: kinetic.py
Author: Brian Phillips

Comput momentum of an object.

Momentum is its mass multiplied by its velocity.
This is a program that accepts an object’s mass
(in kilograms) and velocity (in meters per second)
as inputs and then outputs its momentum.

The kinetic energy of a moving object is given
by the formula KE=(1/2)mv 2 , where m is the
object’s mass and v is its velocity. Modify
the program you created in Project 5 so that
it prints the object’s kinetic energy as well as its momentum.


Inputs: mass      
        velocity 

Outputs:  momentum
         kinetic energy
"""

mass = float(input("Enter the mass in kg: "))
velocity = float(input("Enter the velocity in m/s: "))

momentum = mass * velocity
kineticEnergy = 0.5 * (mass * (velocity ** 2))

print("The momentum is " + str(momentum) + " kg m/s")
print("The kinetic energy is " + str(kineticEnergy) + " Joules")

input("Please press enter or return to quit the program.")





