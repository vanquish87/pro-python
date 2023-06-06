"""
Difference between Two Sets
The difference between two sets A and B include elements 
of set A that are not present on set B.
"""

# first set
A = {2, 3, 5}

# second set
B = {1, 2, 6}

# perform difference operation using &
print("Difference using &:", A - B)

# perform difference operation using difference()
print("Difference using difference():", A.difference(B))
