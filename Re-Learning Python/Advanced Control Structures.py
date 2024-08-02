# Example of a nested loop
for i in range(3):
    for j in range(2):
        print(f"i = {i}, j = {j}")

print("___________________")

# Create a list of squares from 1 to 10 using list comprehension
squares = [x**2 for x in range(1, 11)]
print(squares)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
