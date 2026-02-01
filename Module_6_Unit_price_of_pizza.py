import math
def unit_price(diameter_cm, price_euro):
    radius_m = (diameter_cm / 2) / 100
    area = math.pi * radius_m ** 2
    return price_euro / area
print("Pizza 1:")
diameter1 = float(input("Enter diameter (cm): "))
price1 = float(input("Enter price (euros): "))
print("\nPizza 2:")
diameter2 = float(input("Enter diameter (cm): "))
price2 = float(input("Enter price (euros): "))
unit_price1 = unit_price(diameter1, price1)
unit_price2 = unit_price(diameter2, price2)
print(f"\nPizza 1 unit price: {unit_price1:.2f} euros/m_squared")
print(f"Pizza 2 unit price: {unit_price2:.2f} euros/m_squared")
if unit_price1 < unit_price2:
    print("\nPizza 1 provides better value for money!")
elif unit_price2 < unit_price1:
    print("\nPizza 2 provides better value for money!")
else:
    print("\nBoth pizzas have the same value for money!")