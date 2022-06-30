#Little Codey is aan interplanetary space boxer, who is trying to win championship belts for
#various weight categories on other planets within the solar system. 

#Write a space.py program that helps Codey keep track of their target weight by:
#1) Checks which number planet is equal to.
#2) It should then compute their weight on the destination planet.

venus_gravity = 0.91
mars_gravity = 0.38
jupiter_gravity = 2.34
saturn_gravity = 1.06
uranus_gravity = 0.92
neptune_gravity = 1.19
codey_weight = 185
planet = 3
venus = 1
mars = 2
jupiter = 3
saturn = 4
uranus = 5
neptune = 6

print("I have information for the following planets:\n")
print(" 1. Venus   2. Mars    3. Jupiter")
print(" 4. Saturn  5. Uranus  6. Neptune")

if planet == 1:
    weight = venus_gravity * codey_weight
elif planet == 2:
    weight = mars_gravity * codey_weight
elif planet == 3:
    weight = jupiter_gravity * codey_weight
elif planet == 4:
    weight = saturn_gravity * codey_weight
elif planet == 5:
    weight = uranus_gravity * codey_weight 
elif planet == 6:
    weight = neptune_gravity * codey_weight

print(weight)






