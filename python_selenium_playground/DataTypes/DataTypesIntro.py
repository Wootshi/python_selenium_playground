print("hello world")

# writing comments. We're using # instead of // like JS or Java

a = 3
print(a)

streeng = "Hello World"
print(streeng)

b, c, d = 5, 6.4, "Bruh"
# you can declare variables like that, their values will be assigned
# in this specific order

# print("Value is " + b)
# can't directly concatenate different data types. You can't
# concat str + int

print("{}{}".format('Value is', b))
# similar to String.format in Java

print(type(b), type(c), type(d))
