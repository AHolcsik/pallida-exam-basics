# The program's aim is to collect your favourite animals and store them in a text file.
# There is a given text file called '''favourites.txt''', it will contain the animals
# If ran from the command line without arguments
# It should print out the usage:
# ```fav_animals [animal] [animal]```
# You can add as many command line arguments as many favourite you have.
# One animal should be stored only at once
# Each animal should be written in separate lines
# The program should only save animals, no need to print them

import sys
file_name = 'favourites.txt'

def app_controller():
    if len(sys.argv) == 1:
        print_animals()
    elif len(sys.argv) >= 2:
        add_animal()
    else:
        print('Unsuported argument')

def print_animals():
    try:
        f = open(file_name, 'r')
        for animal in f.readlines():
            print(animal)
            f.close()
    except IOError:
        print('Unable to read file: ', file_name)

def add_animal():
    new_animals = sys.argv[1:]
    f = open(file_name, 'a+')
    for animal in new_animals:
        if animal not in f.readlines():
            try:
                f.write(animal + '\n')
            except IOError:
                print('Unable to read file: ', file_name)


app_controller()

