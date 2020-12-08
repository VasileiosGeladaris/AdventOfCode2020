with open('input') as file:
    lines = file.readlines()
    lines = [line[:len(line)-1] for line in lines]

# PART 1:
hashm = dict()
acc = 0
i = 0
while i < len(lines):
    try:
        if hashm[i]:
            break
    except KeyError:
        hashm[i] = True
        instr = lines[i].split(' ')
        if instr[0] == 'acc':
            acc += int(instr[1])
        elif instr[0] == 'jmp':
            i += int(instr[1])
            continue
        i += 1

print(acc)

# PART 2:
def run(lines):
    hashm = dict()
    acc = 0
    i = 0
    while i < len(lines):
        try:
            if hashm[i]:
                return False
        except KeyError:
            hashm[i] = True
            instr = lines[i].split(' ')
            if instr[0] == 'acc':
                acc += int(instr[1])
            elif instr[0] == 'jmp':
                i += int(instr[1])
                continue
            i += 1
    return acc

indexes = []
for i in range(len(lines)):
    if lines[i][:3] == 'jmp' or lines[i][:3] == 'nop':
        indexes.append(i)

for index in indexes:
    newlines = lines.copy()
    instr = newlines[index].split(' ')
    if instr[0] == 'jmp':
        newlines[index] = 'nop ' + instr[1]
    else:
        newlines[index] = 'jmp ' + instr[1]
    acc = run(newlines)
    if acc != False:
        print(acc)
