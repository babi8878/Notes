# Read the content of a file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Write content to a file
with open('example.txt', 'w') as file:
    file.write("Hello, World!")
