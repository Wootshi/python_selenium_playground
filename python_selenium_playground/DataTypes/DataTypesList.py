values = [1, 2, "bruh", 4, 5]

print(values[0])
# 1 print value of list via index

print(values[-1])
# print last value in list

print(values[1:4])
# print values range

values.insert(3,"chel")
print(values)
# inserting value in the list

values.append("last")
print(values)
# add last

values[0] = "first element"
print(values)
# update first

del values[0]
print(values)
# deleting value by index
