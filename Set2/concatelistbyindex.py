list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

new_list = []

for item1, item2 in zip(list1, list2):
    new_list.append(item1 + item2)

print(new_list)
