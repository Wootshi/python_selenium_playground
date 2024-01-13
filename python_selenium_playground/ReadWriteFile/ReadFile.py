file = open('../test.txt')

# print(file.read())  # read entire file
# print(file.read(1))  # read number of bytes from the file

print(file.readline())
print(file.readline())
# once the line "read", the 'cursor' moves forward
# and you have to account for that

# Print line by line using readline method
line = file.readline()
while line != "":
    print(line)
    line = file.readline()
print("-------------")
file.seek(0)
for line in file.readlines():
    print(line)
# readlines method adds all the lines in the list separately

file.close()
