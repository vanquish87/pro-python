"""
Union of Two Sets
The union of two sets A and B include all the elements of set A and B.
"""
# first set
A = {1, 3, 5}

# second set
B = {0, 2, 4}

# perform union operation using |
print("Union using |:", A | B)

# perform union operation using union()
print("Union using union():", A.union(B))
