# Create a function called `unique_characters` that takes a string as parameter
# and returns a list with the unique letters of the given string
# Create basic unit tests for it with at least 3 different test cases
# print(unique_characters("anagram"))
# Should print out:
# ["n", "g", "r", "m"]

def unique_characters(word):
    if len(word) <=1:
        return [word]
    else:
        all_letters = []
        for letter in word:
            all_letters += letter
            unique = [element for element in all_letters if all_letters.count(element) == 1]
        return unique

