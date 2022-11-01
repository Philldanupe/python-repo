#!/usr/bin/env python3.7

# Python implementation goes here

n = int(input("Enter an integer value: "))

if n % 2 != 0:
   print("Weird")
elif n % 2 == 0 and n>2 and n<6:
   print("Not Weird")
elif n % 2 == 0 and n>5 and n<21:
   print("Weird")
elif n % 2 == 0 and n>20:
   print("Not Weird")
else:
    pass

