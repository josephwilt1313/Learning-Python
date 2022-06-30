#Sal runs the biggest shipping company in the tri-county area
#Sal wants to make sure that every one of his customers has the best, and most affordable experience shipping their packages.
#Build a program that will take the weight of a package and determine the cheapest way to ship that package.
#Sal has several different shipping options
#Ground Shipping: small flat charge plus a rate based on the weight
#Ground Shipping Premium: higher flat charge, not charged for weight.
#Drone Shipping: no flat charge, rate based on weight is triple the rate of ground shipping

#Prices:
    #Ground Shipping: 
        #2lbs or less - $1.50/lb + $20 flat
        #Over 2lbs but less than or equal to 6lb - $3.00/lb + flat
        #Over 6lbs but less than or equal to 10lb - $4.00/lb + flat
        #Over 10lbs - $4.75/lb + flat
    #Ground Shipping Premium only $125 flat charge
    #Drone Shipping, no flat:
        #2lbs or less - $4.50/lb
        #Over 2lbs but less than or equal to 6lb - $9.00/lb
        #Over 6lb but less than or equal to 10lb - $12.00/lb
        #Over 10lbs - $14.25/lb

#Steps:
    #1. Define a weight variable
    #2. Need to know how much it costs to ship a package of given weight by normal ground shipping
        #Write a comment that says "Ground Shipping"
        #Create an if/elif/else statement for the cost of ground shipping. It should check for weight, and print the cost of shipping a package of that weight.
    #3. A package that weighs 8.4 lbs should cost $53.60 to ship with normal ground shipping:
        # 8.4 lb * $4.00 + $20.00 = $53.60: Test it gets the same value
    #4. Create a variable for the cost of premium ground shipping
    #5. Print it out for the user just in case they forgot!
    #6. Write a comment for this section: "Drone Shipping".
    #7. Create an if/elif/else statement for the cost of drone shipping. This statement should check against the weight and print the cost of shipping a package of that weight.
    #8. A package that weighs 1.5 lbs should cost 6.75 to ship by drone:
        #1.5 lbs * $4.50 + $0.00 = $6.75
    #9. What is the cheapest method of shipping a 4.8 pound package and how much would it cost?
        #What is the cheapest method of shipping a 41.5 pound package and how much would it cost?


weight = 8.4
#Ground Shipping
if weight <= 2:
    cost_ground = weight * 1.50 + 20
elif weight <= 6:
    cost_ground = weight * 3.00 + 20
elif weight <= 10:
    cost_ground = weight * 4.00 + 20
else:
    cost_ground = weight * 4.75 + 20
print("Ground Shipping $",cost_ground)

#Ground Shipping Premium
cost_ground_premium = 125
print("Ground Shipping Premium $",cost_ground_premium)

#Drone Shipping

if weight < 2:
    cost_drone = weight * 4.5
elif weight <= 6:
    cost_drone = weight * 9.00
elif weight <= 10:
    cost_drone = weight * 12.00
else:
    cost_drone = weight * 14.25
print("Drone Shipping $",cost_drone)