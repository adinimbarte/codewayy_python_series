# declaration of dictionaries
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

# Accessing elements using keys
print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])

# Add new entry
dict['College'] = " YCCE "
print('dict:', dict)

# remove entry with key 'Name'
del dict['Name']
print('dict:', dict)

# Returns a list of dict's (key, value) tuple pairs
print('dict:', dict.items())

# prints the length of dictionary
print('length of dictionary: ', len(dict))

# to remove  the inserted key-value pair
print("recently added item removed:", dict.popitem())

# sorted key values in alphabetical order
print("sorted dictionary:", sorted(dict))

# prints list of keys
print("List:", list(dict))

