""" set is unordered and also unindexed collection of items in python

dublicates not allowed in set
"""

s={1,2,3,4,"a","b", True}

print(s)

s.add("hi")

s.remove("a")

print(s)

s1={0,9,8,7}

print(s.union(s1))
print(s.intersection(s1))
 


