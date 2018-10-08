# filename     : Marey_e2.py
# author       : Marey Klarize Sevilla
# description  : this is my 2nd exercise python program that prints the content of a dictionary in a specific format

import sys

# Read input 
sustained_winds = sys.argv[1]

# Convert
sustained_winds = float(sustained_winds)

if sustained_winds >= 220.0:
    print("Super Typhoon")
elif sustained_winds >= 110.0:
    print("Typhoon")
else:
    print("I don't know")