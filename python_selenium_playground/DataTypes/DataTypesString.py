str = "Sup_sup check 123"
str1 = "Chel"
str2 = "_sup"

print(str[1])  # u

print(str[0:5])  # substrings

print(str + str1)  # concat

print(str2 in str)  # check if string is present in other string, boolean

var = str.split("_")
print(var)
print(var[0]) # split string, can use spacebar as a separator

str4 = " great "
print(str4.strip()) # trimming
print(str4.lstrip()) # trimming left characters
print(str4.rstrip()) # trimming right