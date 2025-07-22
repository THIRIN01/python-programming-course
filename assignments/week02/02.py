"""
Question 2: Currency Converter (20 points)

Write a program that converts between Thai Baht (THB) and US Dollars (USD).
Requirements:

Ask user to choose conversion direction (THB to USD or USD to THB)
Ask for the amount to convert
Use exchange rate: 1 USD = 35.5 THB
Display result with 2 decimal places
Show the calculation formula used
"""
direction = input("What is your conversion direction (1: THB to USD, 2: USD to THB): ")
amoamount = float(input("Amount to convert: "))
if direction == "1":
    result = amount / 35.5
    print("Result =", round(result, 2))
    print(f"{amount} / 35.5 = {round(result, 2)}")

elif direction == "2":
    result = amount * 35.5
    print("Result =", round(result, 2))
    print(f"{amount} * 35.5 = {round(result, 2)}")

else:
    print("Invalid direction. Please enter 1 or 2.")