# Display available pizza options
print("Welcome to our pizza shop!")
print("We have the following pizza options:")
print("- Small pizza ($8.99)")
print("- Medium pizza ($12.99)")
print("- Large pizza ($15.99)")
print()

# Ask for pizza size
size = input("What size pizza would you like? (S/M/L) ").upper()

# Ask for crust type
crust = input("What type of crust would you like? (Thin/Thick/Stuffed) ").title()

# Ask for toppings
toppings = input("What toppings would you like? (Comma separated) ").title().split(",")

# Calculate the total price
price = 0

if size == "S":
    price = 8.99
elif size == "M":
    price = 12.99
elif size == "L":
    price = 15.99

price += (len(toppings) * 1.5)

# Display the order summary
print("\\nOrder Summary:")
print(f"- Pizza size: {size}")
print(f"- Crust type: {crust}")
print(f"- Toppings: {', '.join(toppings)}")
print(f"- Total price: ${price:.2f}")
