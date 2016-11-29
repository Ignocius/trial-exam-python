# Create a function that takes a filename as string parameter,
# and counts the occurances of the letter "a", and returns it as a number.
# It should not break if the file does not exist, just return 0.

def letter_counter_from_file(file_name):
    try:
        f = open(file_name, "r")
        read = f.readlines()
        a_counter = 0
        for line in range(len(read)):
            for word in read[line]:
                if word == "a":
                    a_counter += 1
        print(a_counter)
    except FileNotFoundError:
        print(0)

letter_counter_from_file("tesst.txt")
