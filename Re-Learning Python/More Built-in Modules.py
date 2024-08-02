import csv
import re

# Writing to a CSV file
with open('example.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerow({'name': 'John', 'age': 30})
    writer.writerow({'name': 'Alice', 'age': 25})

# Reading from a CSV file
with open('example.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['name'], row['age'])



# Search for a pattern in a string
pattern = r"\b[a-zA-Z]{5}\b"
text = "Hello, my name is Alice and I love Python."

matches = re.findall(pattern, text)
print(matches)  # Output: ['Hello', 'Alice']
