# We've decided to pursue the dream of small-business ownership and open up a furniture store called:
# Loveley Loveseats for Neat Suites on Fleet Street.
# Build up a system to help speed up the process of creating reciepts for your customers.
# Storing the names and prices of a furniture store's catalog in variables.
# Then process the total price and item list of customers, printing them to the output terminal
# Remember all variables must be declared before they are referenced in your code

# Step One: Add in the first item, the Lovely Loveseat.

lovely_loveseat_description = """Lovely Loveseat. Tufted Polyester
blend on word. 32 inches high x 40 inches wide x 30 inches deep. Red or white."""

#Step Two: Create a price for the loveseat.

lovely_loveseat_price = 254.00

#Step 3: Extend inventory with another piece of furniture.

stylish_settee_description = """Stylish Settee. Faux leather on birch. 29.50 inches high x
54.75 inches wide x 28 inches deep. Black"""

# Step 4: Create the price for the Stylish Settee

stylish_settee_price = 180.50

#Step 5: Add one more item to the business.

luxurious_lamp_description= """Luxurious Lamp. Glass and Iron. 36 inches tall. Brown with cream shade."""

# Step 6: Set price of the lamp.

luxurious_lamp_price = 52.15

#Step 7: Define variable sales tax

sales_tax = .088

#Step 8: First Customer purchase

customer_one_total = 0

#Step 9: List of purchases

customer_one_itemization = ""

customer_one_total += lovely_loveseat_price

customer_one_itemization += lovely_loveseat_description

customer_one_total += luxurious_lamp_price

customer_one_itemization += luxurious_lamp_description

customer_one_tax = (customer_one_total * sales_tax)

customer_one_tax + customer_one_total

print("Customer One Items:")
print(customer_one_itemization)
print("Customer One Total: ")
print(customer_one_total)