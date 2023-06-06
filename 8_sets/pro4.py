"""
Set Symmetric Difference
The symmetric difference between two sets A and B includes 
all elements of A and B without the common elements.
"""

# first set
A = {2, 3, 5}

# second set
B = {1, 2, 6}

# perform difference operation using &
print("using ^:", A ^ B)

# using symmetric_difference()
print("using symmetric_difference():", A.symmetric_difference(B))
