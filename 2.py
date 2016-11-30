# Create a function that takes a filename as string parameter,
# and counts the occurances of the letter "a", and returns it as a number.
# It should not break if the file does not exist, just return 0.

def letterA_counter_from_file(file_name):
    try:
        f = open(file_name)
        readall = f.readlines()
        a_counter = 0
        for word in range(len(readall)):
            for char in readall[word]:
                if char == "a":
                    a_counter +=1
        return a_counter

    except FileNotFoundError:
        print("File not found!")

print(letterA_counter_from_file("test.txt"))
