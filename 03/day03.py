import math

with open('input') as file:
    lines = file.readlines()
    lines = [line[:len(line)-1] for line in lines]

# PART 1:
count1 = 0
pos = 0
for line in lines:
    if line[pos] == '#':
        count1 += 1
    pos = (pos + 3) % len(line)

print(count1)

# PART 2:
def check_slope(right, down):
    count = 0
    pos = 0
    i = 0
    while i < len(lines):
        if lines[i][pos] == '#':
            count += 1
        pos = (pos + right) % len(line)
        i += down
    return count

results = []
results.append(check_slope(1, 1))
results.append(check_slope(3, 1))
results.append(check_slope(5, 1))
results.append(check_slope(7, 1))
results.append(check_slope(1, 2))

print(f'{results[0]} * {results[1]} * {results[2]} * {results[3]} * {results[4]} = {math.prod(results)}')
