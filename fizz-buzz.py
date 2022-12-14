#!/usr/bin/env python3.7
# Create a Range from 1 to the User's Provided Number and Loop Through It
# Print "FizzBuzz" if the Value Is a Multiple of Three and Five
# Print "Fizz" if the Value Is a Multiple of Three and "Buzz" if It's a Multiple of Five

upper_number = int(input("How many values should we process: "))

for number in range(1, upper_number + 1):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)