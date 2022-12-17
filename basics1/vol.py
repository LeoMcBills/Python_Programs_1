'''Calculation for a volume of a sphere'''

radius = int(input("Enter the radius of the given sphere: "))
r = radius
const = (4 / 3)
pi = 3.141592653589793238
vol = const * pi * (r*r*r)

print("Volume: ", vol)