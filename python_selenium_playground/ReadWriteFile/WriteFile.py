file = open('test.txt')

file.close()

# This is better in order to work with files.
# File operations remain within the 'with' statement
with open('test.txt', 'r') as reader:
    # 'r' flag means that file is in read mode
    # read mode is the default
    content = reader.readlines()
    print(list(reversed(content)))
    print(content)
    print("------")
    with open('test.txt', 'w') as writer:
        # we're opening the same file, and using 'content' from the file
        # the content already exists in memory
        # we're reversing content, and writing the each line in the source file
        # resulting in same lines written in the file in reverse order
        for line in reversed(content):
            writer.write(line)

print(list(reversed(content)))
print(content)
