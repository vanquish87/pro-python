"""
The update() method is used to update the set with items other 
collection types (lists, tuples, sets, etc). For example,
"""

companies = {"Lacoste", "Ralph Lauren"}
tech_companies = ["apple", "google", "apple"]

companies.update(tech_companies)

print(companies)

# Output: {'google', 'apple', 'Lacoste', 'Ralph Lauren'}
