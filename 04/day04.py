import re

with open('input') as file:
    lines = file.readlines()
    lines = [line[:len(line)-1] for line in lines]

required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

# PART 1:
counter = 0
fields = set()
for line in lines:
    if line == '':
        if (fields & required) == required:
            counter += 1
        fields = set()
    else:
        fields = fields.union(set([field[:3] for field in line.split(' ')]))

print(counter)

# PART: 2
def checkByr(number):
    return (1920 <= int(number) <= 2002)

def checkIyr(number):
    return (2010 <= int(number) <= 2020)

def checkEyr(number):
    return (2020 <= int(number) <= 2030)

def checkHgt(number):
    if len(number) == 5 and number.endswith("cm") and (150 <= int(number[:3]) <= 193):
        return True
    if len(number) == 4 and number.endswith("in") and (59 <= int(number[:2]) <= 76):
        return True
    return False

def checkHcl(color):
    if len(color) == 7 and color[0] == '#' and bool(re.match("^[a-f0-9]*$", color[1:])):
        return True
    return False

def checkEcl(color):
    if color in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return True
    return False

def checkPid(pid):
    if len(pid) == 9 and 0 <= int(pid) <= 999999999:
        return True
    return False

def checkCid(cid):
    return True

check = {
    "byr": checkByr,
    "iyr": checkIyr,
    "eyr": checkEyr,
    "hgt": checkHgt,
    "hcl": checkHcl,
    "ecl": checkEcl,
    "pid": checkPid,
    "cid": checkCid
}

counter = 0
fields = set()
valid = True
for line in lines:
    if line == '':
        if valid and (fields & required) == required:
            counter += 1
        fields = set()
        valid = True
    else:
        if not valid:
            continue
        for field in line.split(' '):
            record = field.split(':')
            if not (check[record[0]])(record[1]):
                fields = set()
                valid = False
                break
            fields.add(record[0])

print(counter)
