# Sample list increment
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

# List comprehension version
# new_list = [new_item for item in list if test]
numbers_comprehension = [1, 2, 3]
new_list = [n + 1 for n in numbers_comprehension]
