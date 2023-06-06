"""
Check if two sets are equal
We can use the == operator to check whether two sets are equal or not. 
"""

# first set
A = {1, 3, 5}

# second set
B = {3, 5, 1}

# perform difference operation using &
if A == B:
    print("Set A and Set B are equal")
else:
    print("Set A and Set B are not equal")
