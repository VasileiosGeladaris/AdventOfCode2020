with open('input') as file:
    lines = file.readlines()
    lines = [line[:len(line)-1] for line in lines]

# PART 1:
from itertools import combinations

def find_first():

    def check(val):
        return sum(val) == num

    for i in range(25, len(lines)):
        num = int(lines[i])
        preamble = list(map(int, lines[i-25:i]))
        combs = list(filter(check, list(combinations(preamble, 2))))
        if not combs:
            return num

num = find_first()
print(num)

# PART 2:
def find_weakness():
    nums = list(map(int, lines))
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            c_set = nums[i:j]
            c_sum = sum(c_set)
            if c_sum > num:
                break
            elif c_sum == num:
                return min(c_set) + max(c_set)

print(find_weakness())
