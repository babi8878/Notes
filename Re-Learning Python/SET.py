# Create a set
fruits = {"apple", "banana", "cherry"}
print(fruits)

# Add an element to a set
fruits.add("orange")
print(fruits)

# Remove an element from a set
fruits.remove("banana")
print(fruits)

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union
print(set1 | set2)  # Output: {1, 2, 3, 4, 5}

# Intersection
print(set1 & set2)  # Output: {3}

# Difference
print(set1 - set2)  # Output: {1, 2}
