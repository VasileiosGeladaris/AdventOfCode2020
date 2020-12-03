# Read file, create an array of its values after removing the \n from each line
with open('input') as file:
    values = file.readlines()
    values = [int(value[:len(value)-1]) for value in values]

# Create a hashmap of every value's complements to reach 2020.
# When you encounter that complement in the future, multiply the two together and print them.
complements = dict()
for i, value in enumerate(values):
    try:
        print(f'{values[complements[value]]} * {value} = {value * values[complements[value]]}')
    except KeyError:
        complements[2020 - value] = i
