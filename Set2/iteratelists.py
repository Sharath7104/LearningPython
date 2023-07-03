list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

list2_reverse = list2[::-1]

for item1, item2 in zip(list1, list2_reverse):
    print(item1, item2)
