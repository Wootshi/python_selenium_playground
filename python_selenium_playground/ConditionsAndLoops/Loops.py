obj = [2, 3, 5, 7, 9]

for i in obj:
    print(i * 2)

# sum of first nat. number 1+2+3+4+5 = 15
summary = 0

for j in range(1, 6):
    print(j)
    summary = summary + j
print("{}{}".format("Summary is: ", summary))
print("-----------")

# skip some iterations, in this case it will skip over 5 iterations
for k in range(1, 10, 5):
    print(k)
print("------------")

# this will print 0 - 9
for m in range(10):
    print(m)
