# Create a list with initial grades
grades = [85, 92, 78, 95, 83]

# Add a new grade of 90
grades.append(90)

# Sort the grades in ascending order
grades.sort()

# Print the results
print("Sorted grades:", grades)
print("Highest grade:", grades[-1])
print ("Lowest grade:", grades[0])
print("Total number of grades:", len(grades))

# Create the shopping cart
cart = ["apple", "banana", "milk", "bread", "apple", "eggs"]

# Count how many times "apple" appears
print("Number of apples:", cart.count("apple"))

# Find the position of milk
print("Position of milk:", cart.index("milk"))

# Remove one apple from the cart
cart.remove("apple")

# Remove and print hte last item using pop()
print("Removed item using pop:", cart.pop())

# Check if "banana" is in the cart
print("Is banana in the cart?", "banana" in cart)

# Print the final cart
print("Final cart:", cart)

# Create tuples for coordinate points
point1 = (3, 5)
point2 = (7, 2)

# Unpack the tuples into variables
x1, y1 = point1
x2, y2 = point2

# Print hte points and unpacked values
print("Point 1:", point1)
print("Point 2:", point2)
print(f"x1 = {x1}, y1 = {y1}")
print(f"x2 = {x2}, y2 = {y2}")

# Calculate the distance between points
distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print("Distance between points:", distance)

# Create a tuple from the string using a tuple() constructor
python_tuple = tuple("PYTHON")
print("Characters tuple:", python_tuple)

# Print each character using a for loop
for char in python_tuple:
    print(char)

# Create sets for class attendance
monday_class = {"Alice", "Bob", "Charlie", "Diana"}
wednesday_class = {"Bob", "Diana", "Eve", "Frank"}

# Add "Grace" to monday_class
monday_class.add("Grace")

# Print the classes
print("Monday class:", monday_class)
print("Wednesday class:", wednesday_class)

# Find students who attended both classes (intersection)
print("Attended both classes:", monday_class & wednesday_class)

# Find students who attended either class (union)
all_students = monday_class | wednesday_class
print("Attended either class:", all_students)

# Find students who attended only Monday (difference)
print("Only Monday:", monday_class - wednesday_class)

# Find students who attended only one class, not both (symmetric difference)
print("Only one class (not both):", monday_class ^ wednesday_class)

# Check if monday_class is a subset of the union
print("Is Monday subset of all students?", monday_class <= all_students)

# Create the contacts dictionary
contacts = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9999"
}

# Print Alice's phone number
print("Alice's number:", contacts["Alice"])

# Add a new contact: Diana
contacts["Diana"] = "555-4321"
print("Contacts after adding Diana:", contacts)

# Update Bob's number
contacts["Bob"] = "555-0000"
print("Contacts after updating Bob:", contacts)

# Delete Charlie's contact
del contacts["Charlie"]
print("Contacts after deleting Charlie:", contacts)

# Print all contact names using keys()
print("All names:", contacts.keys())

# Print all phone numbers using values()
print("All numbers:", contacts.values())

# Print total number of contacts
print("Total contacts:", len(contacts))

# Create the inventory dictionary with tuples (price, quantity)
inventory = {
    "Laptop": (999.99, 5),
    "Mouse": (29.99, 15),
    "Keyboard": (79.99, 10),
    "Monitor": (299.99, 8)
}

# Print current inventory
print("=== Current Inventory ===")
for product, details in inventory.items():
    price, quantity = details
    print(f"{product} - Price: ${price}, Quantity: {quantity}")

# Create category sets
electronics = {"Laptop", "Monitor"}
accessories = {"Mouse", "Keyboard"}

# Find all products using union
all_categories = electronics | accessories
print(f"\nAll product categories: {all_categories}")

# Create a list of all prices (extract from tuples)
price_list = [details[0] for details in inventory.values()]
print(f"\nPrice list: {price_list}")

# Sort prices and print lowest/highest
sorted_prices = sorted(price_list)
print(f"Sorted prices: {sorted_prices}")
print(f"Lowest price: ${sorted_prices[0]}")
print(f"Highest price: ${sorted_prices[-1]}")

# Add new product
inventory["Headphones"] = (49.99, 20)

# Update Mouse quantity (keep same price)
inventory["Mouse"] = (29.99, 12)

# Remove Monitor from inventory
del inventory["Monitor"]

# Print final inventory
print("\n=== Final Inventory ===")
for product, details in inventory.items():
    price, quantity = details
    print(f"{product} - Price: ${price}, Quantity: {quantity}")
