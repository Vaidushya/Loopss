# Welcome message
print("Welcome to the Power Calculator!")

# Ask the user for the number of calculations
n = int(input("Enter the number of input you want to calculate: "))

# Perform the power calculations
for i in range(n):
    base = float(input(f"Enter the base for calculation: "))
    exponent = float(input(f"Enter the exponent for calculation: "))
    result = base ** exponent
    print(f"{base} raised to the power of {exponent} is {result}")

# End message
print("All calculations completed! Thank you for using the Power Calculator.😊")
