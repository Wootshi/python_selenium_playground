itemsInCart = 0

if itemsInCart != 2:
    # raise is basically Java's "throw"
    # raise Exception("Exception text")
    pass

assert (itemsInCart == 0)
# your favorite, assertion

try:
    with open('../ee.txt', 'r') as reader:
        reader.read()
except:
    # this is Java's try-catch, here's try-except
    print("Exception text in a try-except")

try:
    with open('../test.txt', 'r') as reader:
        reader.read()
except Exception as e:
    # That's how you're specifying an Exception. This does not fail the program
    print(e)

finally:
    # 'When a return, break or continue statement is executed
    # in the try suite of a try...finally statement,
    # the finally clause is also executed ‘on the way out.’
    # Same as in Java
    print("cleaning up resources")
