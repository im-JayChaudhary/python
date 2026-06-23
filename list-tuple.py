# l = [1,2,3,4,5,6]
#list comprehension
# l1 = []
# l1 = [i]
# l1 = [i for i in xyz]
# xyz = range or xyz = other list

# list comprehension with range
l1 = [i for i in range(9)]
print(l1)

# list comprehension with other list
l2 = [i*i for i in l1]
print(l2)

# list comprehension with condition
l3 = [i+2 for i in l1 if i%5==0]
print(l3)

# # list methods here
# l = l1.copy()
# print(l)

l = [1,2,3,4,5,6,7]

print(l.append(7))
print(l)

print(l.count(7))

print(l.index(7))

l.sort()
print(l)

l.sort(reverse=True)
print(l)

l.extend([l2])
print(l)

l.append(8)
print(l)

# l = [7, 7, 6, 5, 4, 3, 2, 1, [0, 1, 4, 9, 16, 25, 36, 49, 64], 8]

# # Flatten the list
# flattened = []
# for item in l:
#     if isinstance(item, list):
#         flattened.extend(item)
#     else:
#         flattened.append(item)

# flattened.sort()
# print(flattened)  # [0, 1, 1, 2, 3, 4, 4, 5, 6, 7, 7, 8, 9, 16, 25, 36, 49, 64]

# l = [7, 7, 6, 5, 4, 3, 2, 1, [0, 1, 4, 9, 16, 25, 36, 49, 64], 8]

# # Extract only numbers
# numbers = [item for item in l if not isinstance(item, list)]
# numbers.sort()
# print(numbers)  # [1, 1, 2, 3, 4, 5, 6, 7, 7, 8]

# l = [7, 7, 6, 5, 4, 3, 2, 1, [0, 1, 4, 9, 16, 25, 36, 49, 64], 8]

# # Sort by putting lists at the end
# l.sort(key=lambda x: (isinstance(x, list), x))
# print(l)  # Numbers first, list at the end



# tuple

t1 = (1,2,3,4,5,6)
print(t1[0])

# t1.append(7) # This will raise an AttributeError because tuples are immutable

print(t1.count(1))  # Returns the number of occurrences of 1 in the tuple
print(t1.index(3))  # Returns the index of the first occurrence of 3 in the tuple

# tuples are immutable, so you cannot add or remove elements from them. 
# However, you can create a new tuple by concatenating existing tuples.
t2 = (7, 8, 9)
t3 = t1 + t2
print(t3)

# to edit a tuple, you would need to convert it to a list, 
# make the changes, and then convert it back to a tuple. For example:
t4 = list(t1)
t4.append(7)
t1 = tuple(t4)
print(t1)

# while tuples are immutable, they can contain mutable objects like lists.
t5 = (1, 2, [3, 4])
print(t5)

# You can modify the mutable object (the list) inside the tuple:
t5[2].append(5)
print(t5)

# there can not be a tuple inside a list, but there can be a list inside a tuple.
# because tuples are immutable, they can be used as keys in dictionaries, while lists cannot.
lwithtuple = [(1, 2), (3, 4), (5, 6)]
lwithtuple.append((7, 8))
print(lwithtuple)
lwithtuple.append(9)
print(lwithtuple[1])
# lwithtuple[1].append(10)  # This will raise an AttributeError because tuples are immutable
# lwithtuple[1] = (10, 11)  # This will raise a TypeError because tuples are immutable

t = (1, 2, 3, 4, 5)

print(*t, sep=', ')        # 1, 2, 3, 4, 5
print(*t, sep=' | ')       # 1 | 2 | 3 | 4 | 5
print(*t, sep='\n')        # prints each on new line
print(*t, sep='---')       # 1---2---3---4---5