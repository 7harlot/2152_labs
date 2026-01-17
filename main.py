# lab 1 
# ben morrison, 101572409 

# Define Variables: Array with elements 1, 4, 7, 9 
# in python, we use lists instead of arrays
numbers = [1, 4, 7, 9]

# Order of Operations: define variables "a, b, c, d" 
a = 1
b = 2
c = 3
d = 4

# Fully-bracketed expression of: e = a * c - b / d 
e = (a * c) - (b / d)
print(f"First equation result: {e}")

# Fully-bracketed version of: e = a - b ** c // d + a % c 
# Broken down by operator precedence:
# 1. ** (exponentiation)
# 2. // (floor division)
# 3. % (modulus)
# 4. - (subtraction)
# 5. + (addition)
e = (((a - (b ** c)) // d) + (a % c))
print(f"Second equation result: {e}")

# Formatting: Temperature variable with format function 
temperature = 32.6
print("The temperature is: " + "{:.2f}".format(temperature) + " degrees Celsius")

# Common functions: User input and age filtering
userAge = int(input("Enter age: "))
userAge = userAge + 22
print(f"Now showing the shop items filtered by age: {userAge}")
