#File Handling
#Explanation: File handling allows reading from and writing to files on the filesystem.

#File Modes
'r' - Read (default)

'w' - Write (overwrites)

'a' - Append

'x' - Exclusive creation

'b' - Binary mode

't' - Text mode (default)

'+' - Read and write

#Reading Files

# Reading entire file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Reading line by line
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())

# Reading all lines into list
with open('example.txt', 'r') as file:
    lines = file.readlines()
    print(lines)

# Reading specific number of characters
with open('example.txt', 'r') as file:
    chunk = file.read(10)  # Read first 10 characters
    print(chunk)

# Using seek and tell
with open('example.txt', 'r') as file:
    print(file.tell())     # Current position
    file.seek(5)           # Move to position 5
    print(file.read(10))
#Writing Files

# Writing to file (overwrites if exists)
with open('output.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is a new line\n")

# Appending to file
with open('output.txt', 'a') as file:
    file.write("Appending this line\n")

# Writing multiple lines
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open('output.txt', 'w') as file:
    file.writelines(lines)

# Using print to write
with open('output.txt', 'w') as file:
    print("Hello", "World", file=file)
    print("Another line", file=file)
#Working with Binary Files

# Writing binary data
data = b'\x48\x65\x6c\x6c\x6f'  # "Hello" in bytes
with open('binary.bin', 'wb') as file:
    file.write(data)

# Reading binary data
with open('binary.bin', 'rb') as file:
    content = file.read()
    print(content)  # b'Hello'

# Copying binary file
with open('source.bin', 'rb') as source:
    with open('destination.bin', 'wb') as dest:
        dest.write(source.read())
