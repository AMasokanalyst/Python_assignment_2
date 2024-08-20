# Creating an empty list called my_list.
my_list = []

# Appending 10, 20, 30, 40 to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Inserting 15 at the second position of my_list
my_list.insert(1, 15)

# Extending my_list with a list that have values [50, 60, 70]
my_list.extend([50, 60, 70])

# Removing the last element of my_list
my_list.pop()

# Sorting my_list in ascending order
my_list.sort(reverse=False)
# Finding the index of element 30 in my_list
print(my_list.index(30))

print(my_list)