with open('input') as file:
    lines = file.readlines()
    lines = [line[:len(line)-1] for line in lines]

# PART 1:
diff1 = 0
diff3 = 0
adapters = sorted(list(map(int, lines)))
adapters.insert(0, 0)
adapters.append(adapters[len(adapters)-1] + 3)

for i in range(1,len(adapters)):
    diff = adapters[i] - adapters[i-1]
    if diff == 1:
        diff1 += 1
    elif diff == 3:
        diff3 += 1

print(diff1 * diff3)

# PART 2:
hashm = dict()
hashm[0] = 1
for i in range(len(adapters)):
    for j in range(1,4):
        try:
            hashm[adapters[i] + j] += hashm[adapters[i]]
        except KeyError:
            hashm[adapters[i] + j] = hashm[adapters[i]]

print(hashm[adapters[len(adapters)-1]])
