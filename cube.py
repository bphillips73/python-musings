"""
Program: cube.py
Author: Brian Phillips

Compute surface area of a cube 

1. The inputs is
       length
       
3. Computations:
       surfaceArea = length * length * 6 (six sided cube)
       
4. The outputs are
       surfaceArea
"""

              
# Request the inputs
length = float(input("Enter the known length of the edge: "))
  

# Compute the area 
surfaceArea = length * length * 6 #(six sided cube)
         
# Display the income tax
print("The surface area is " + str(surfaceArea) + " square units.")
