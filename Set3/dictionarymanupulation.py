def add_person(dictionary, name, age):
    dictionary[name] = age

def update_age(dictionary, name, age):
    if name in dictionary:
        dictionary[name] = age

def delete_person(dictionary, name):
    if name in dictionary:
        del dictionary[name]

# Test case
people = {}
add_person(people, "John", 25)
print(people)  # Output: {'John': 25}

update_age(people, "John", 26)
print(people)  # Output: {'John': 26}

delete_person(people, "John")
print(people)  # Output: {}
