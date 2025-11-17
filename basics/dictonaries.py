# Dictionary of chai types
chai_types = {
    'masala': 'spicy',
    'ginger': 'zesty',
    'green': 'mild'
}

print(chai_types)

# Accessing values
print(chai_types['ginger'])
print(chai_types.get('masala'))

# Updating a value
chai_types['green'] = 'fresh'
print(chai_types)

# Loop through keys
for chai in chai_types:
    print(chai, chai_types[chai])

# Loop using items()
for key, value in chai_types.items():
    print(key, value)

# Adding a new value
chai_types['Earl Grey'] = "citrus"
print(chai_types)

# Removing items
chai_types.pop("ginger")  # removes ginger
print(chai_types)

chai_types.popitem()  # removes the last inserted item
print(chai_types)

# Copy dictionary
chai_types_copy = chai_types.copy()

# Dictionary comprehension
squared_num = {x: x**2 for x in range(6)}
print(squared_num)

# Clearing a dictionary
squared_num.clear()
print(squared_num)
