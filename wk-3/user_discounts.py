def calculate_discount(price, discount_percent):
    # Check if discount is 20% or higher
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# --- Get user input ---
# Get the original price
price_input = float(input("Enter the original price: "))
# Get the discount percentage
discount_input = float(input("Enter the discount percentage: "))

# --- Calculate and print result ---
final_price = calculate_discount(price_input, discount_input)

if discount_input >= 20:
    print(f"Discount applied! Final price: {final_price}")
else:
    print(f"No discount applied. Final price: {final_price}")
