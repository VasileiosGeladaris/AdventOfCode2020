with open('input') as file:
    lines = file.readlines()
    lines = [line[:len(line)-1] for line in lines]

# PART 1:
i = 0
counter = 0
questions = set()
while i < len(lines):
    for q in lines[i]:
        questions.add(q)
    try:
        if lines[i+1] == '':
            counter += len(questions)
            questions = set()
            i += 1
    except IndexError:
        counter += len(questions)
    i += 1

print(counter)


# PART 2:
i = 0
counter = 0
common = set()
questions = set()
flag = True
while i < len(lines):
    for q in lines[i]:
        questions.add(q)
    if flag:
        common = questions
        flag = False
    else:
        common = common.intersection(questions)
    questions = set()
    try:
        if lines[i+1] == '':
            counter += len(common)
            common = set()
            flag = True
            i += 1
    except IndexError:
        counter += len(common)
    i += 1

print(counter)
