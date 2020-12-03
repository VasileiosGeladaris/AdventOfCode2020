import re

with open('input') as file:
    lines = file.readlines()
    lines = [line[:len(line)-1] for line in lines]

# PART 1:
sum = 0
for line in lines:
    params = re.split('-| |: ', line)
    if int(params[0]) <= params[3].count(params[2]) <= int(params[1]):
        sum += 1

print(sum)

# PART 2:
sum = 0
for line in lines:
    params = re.split('-| |: ', line)
    if (params[3][int(params[0])-1] == params[2]) ^ (params[3][int(params[1])-1] == params[2]):
        sum += 1

print(sum)
