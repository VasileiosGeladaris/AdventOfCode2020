with open('input') as file:
    lines = file.readlines()
    lines = [line[:len(line)-1] for line in lines]

# PART 1:
def read_bpass(less, more, arr, path):
    if len(arr) == 1:
        return arr[0]
    letter = path[0]
    if letter == less:
        return read_bpass(less, more, arr[:int(len(arr)/2)], path[1:])
    elif letter == more:
        return read_bpass(less, more, arr[int(len(arr)/2):], path[1:])

max = -1
for line in lines:
    id = read_bpass('F', 'B', range(128), line[:7]) * 8 + read_bpass('L', 'R', range(8), line[7:])
    if id > max:
        max = id

print(max)

# PART 2:
from itertools import product

# Get all possible combinations for a passport.
combs = [''.join(comb1) + ''.join(comb2) for comb1 in product(['F', 'B'], repeat=7) for comb2 in product(['L', 'R'], repeat=3)]

# Get all the missing passports from the input.
missing = [x for x in combs if x not in lines]

# Get the row path for each missing passport.
missing_rows = [x[:7] for x in missing]

# Find the one row with the only empty seat.
row = min(missing_rows, key = missing_rows.count)
passp = missing[missing_rows.index(row)]

# Print the seat's ID.
id = read_bpass('F', 'B', range(128), passp[:7]) * 8 + read_bpass('L', 'R', range(8), passp[7:])
print(id)
