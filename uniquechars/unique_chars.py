# Create a function called `unique_characters` that takes a string as parameter
# and returns a list with the unique letters of the given string
# Create basic unit tests for it with at least 3 different test cases
# print(unique_characters("anagram"))
# Should print out:
# ["n", "g", "r", "m"]

def unique_characters(str):
    unique = []
    for letter in str:
        if letter in unique:
            unique.remove(letter)
        if letter not in unique:
            unique += letter
    return unique

print(unique_characters("anagram"))


