tuple1 = (11, [22, 33], 44, 55)

list1 = list(tuple1)  # Convert tuple to list
list1[1][0] = 222  # Modify the first item of the list inside the tuple
tuple1 = tuple(list1)  # Convert list back to tuple

print(tuple1)
