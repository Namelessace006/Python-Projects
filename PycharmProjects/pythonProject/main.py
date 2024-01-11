import random
# # To add the two digits of a two-digit number
#
# number = input("Input a two-digit number: ")
# num = int(number[0]) + int(number[1])
# print(f"{number[0]} + {number[1]} = {num}")
#
# # A Body Mass Index Calculator
# weight = float(input("Input your weight in KG: "))
# height = float(input("Input your height in M: "))
# BMI = int(weight//(height**2))
# print(f"Your Body Mass Index is {BMI}")
#
# # Your Life Countdown
# age = int(input("Enter your current age: "))
# years_left = 90 - age
# months_left = 1080 - (age * 12)
# weeks_left = 4680 - (age * 52)
# # without using leap year...
# days_left = 32850 - (age * 365)
# # using leap year...
# day_left = 32872 - ((age * 365) + (age // 4))
# print(f"You have {days_left} days, {weeks_left} weeks, {months_left} months and {years_left} years till you're 90 years.")
#
# # A Tip Calculator
# bill = int(input("What was the total bill: #"))
# tip_percentage = int(input("How much tip would you like to give: 10, 12 or 15\t"))
# people_split = int(input("How many people are to split the bill? "))
# if tip_percentage == 10:
#     t_bill = float(bill * 0.1) // people_split
#     print(f"Each person should pay #{t_bill}k")
# elif tip_percentage == 12:
#     t_bill = float(bill * 0.12) // people_split
#     print(f"Each person should pay #{t_bill}k")
# elif tip_percentage == 15:
#     t_bill = float(bill * 0.15) // people_split
#     print(f"Each person should pay #{t_bill}k")
# else:
#     t_bill = float(bill * (tip_percentage/100)) // people_split
#     print(f"Each person should pay #{t_bill}k")
#
# # To Check if a number is Odd or Even
# Num = float(input("Enter a number: "))
# if Num % 2 == 0:
#     print(f"""The number is EVEN
# {Num} / 2 = {Num / 2}""")
# else:
#     print(f"""The number is ODD
# {Num} / 2 = {Num / 2}""")
#
# # BMI Calculator 2.0
# height = float(input("Enter your height in M: "))
# weight = float(input("Enter your weight in KG: "))
#
# BMI = (weight / (height ** 2))
# if BMI < 18.5:
#     print("You are Underweight")
# elif 18.5 > BMI < 25:
#     print("You are Normal Weight")
# elif 25 > BMI < 30:
#     print("You are Overweight")
# elif 30 > BMI < 35:
#     print("You are Obese")
# else:
#     print("You are Clinically Obese")
#
# year = int(input("Enter a Year: "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("The Year is Leap")
#         else:
#             print("Not Leap")
#     else:
#         print("Leap Year")
# else:
#     print("The Year is not Leap")
#
# print("Welcome to Python Pizza Deliveries")
# size = input("What size of Pizza do you want? S, M, L: ").upper()
# pepperoni = input("Do you want pepperoni? Y or N: ").upper()
# cheese = input("Do you want extra cheese? Y or N: ").upper()
# bill = 0
# if size == "S":
#     bill += 15000
#     print("d")
# if size == "M":
#     bill += 20000
#     print("f")
# if size == "L":
#     bill += 30000
#
# if pepperoni == "Y":
#     if size == "S":
#         bill += 3000
#     elif size == "M" or "L":
#         bill += 5000
#     else:
#         print("Invalid Input")
#
# if cheese == "Y":
#     bill += 2000
#
# print(f"Your total bill is #{bill}")
#
#
# # Love Calculator
# print("Welcome to the Love Calculator")
# name1 = input("What is your name?\n").lower()
# name2 = input("What is their name?\n").lower()
# name = name1 + name2
#
# T = name.count("t")
# R = name.count("r")
# U = name.count("u")
# E = name.count("e")
#
# true = T + R + U + E
# print(true)
# L = name.count("l")
# O = name.count("o")
# V = name.count("v")
# E = name.count("e")
#
# love = L + O + V + E
# print(love)
# true_love = str(true) + str(love)
# print(f"Your love score is {true_love}")
#
# # learning how to pick random numbers
# p = random.randint(0, 10)
# print(p)
# # random.random() picks numbers from 0 - 1 without including 1
# # you can increase the range of number it chooses by multiplying the assigned variable by a number of your choice
# q = random.random()
# print(q)
# q = int(q * 10)
# print(q)
#
# # Virtual Coin Toss Program
# guess = random.randint(0, 1)
# if guess == 1:
#     print("Heads")
# else:
#     print("Tails")

# # Difference between ".append()" and ".extend()"
# states = ["Maryland", "Pennslyvania", ["Oklahoma", "Arizona"]]
# states.extend(["Pencilvania", "Angelaland"])
# print(states)
# print(states[-1])
#
# # Who will pay the bill?
# names = input("Enter the names of the people: ")
# name = names.split(", ")
# Name = len(name)
# rand_name = random.randint(0, Name - 1)
# payer = name[rand_name]
# print(f"{payer} should pay the bills")
# print(random.choice(name))
