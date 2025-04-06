integers = open("integers.txt", "r")
contents = integers.read()
integers.close()

# Convert the contents into a list of integers
numbers = contents.split()
numbers = [int(num) for num in numbers]

# Create the output files
double = open("double.txt", "w")
triple = open("triple.txt", "w")

# Process each number
for num in numbers:
    if num % 2 == 0:
        double.write(str(num ** 2) + "\n")
    else:
        triple.write(str(num ** 3) + "\n")

# Close the output files
double.close()
triple.close()
