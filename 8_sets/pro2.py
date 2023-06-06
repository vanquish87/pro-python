"""
Set Intersection
The intersection of two sets A and B include the common elements between set A and B.
"""

# first set
A = {1, 3, 5}

# second set
B = {1, 2, 3}

# perform intersection operation using &
print("Intersection using &:", A & B)

# perform intersection operation using intersection()
print("Intersection using intersection():", A.intersection(B))
