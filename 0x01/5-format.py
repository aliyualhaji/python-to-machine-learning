#!/usr/bin/python3
"""A module for print formating"""

price = 9.99
name = "John Doe"
firstname = "Aliyu"
lastname = "Adam"

print(f'{firstname}+{lastname}')
print(f'The Price of the Product is {price:05}')
print("The Price of the Product is {}".format(price))
print(firstname +' '+ lastname)

print("Hello\n"*3)
print(f"{name} bought a product approximately {price:.0f} Naira")