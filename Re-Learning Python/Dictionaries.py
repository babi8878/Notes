# Create a dictionary
person = {"name": "John", "age": 30}

# Access dictionary items
print(person["name"])  # Output: John

# Modify dictionary items
person["age"] = 31
print(person)  # Output: {'name': 'John', 'age': 31}

# Add items to the dictionary
person["city"] = "New York"
print(person)  # Output: {'name': 'John', 'age': 31, 'city': 'New York'}

# Loop through a dictionary
for key, value in person.items():
    print(f"{key}: {value}")
