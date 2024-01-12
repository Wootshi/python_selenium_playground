it = 10

# while it > 1:
#     print(it)
# infinite loop, no infinite protection in python apparently?

while it > 1:
    if it == 9:
        it = it - 1
        continue
    if it == 3:
        break
    print(it)
    it = it - 1

print("While loop done")
