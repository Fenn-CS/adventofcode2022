# Problem statement: https://adventofcode.com/2022/day/1
callory_sums = []
elf_meal_groups = [] # Holds an array for calories for each elf
temp = []
sum = 0
with open('input', 'r') as input:
    for line in input:
        if line in ['\n', '\r\n']:
            elf_meal_groups.append(temp)
            callory_sums.append(sum)
            sum = 0
            temp = []
        else:
            temp.append(int(line))
            sum = sum + int(line)
# Part 1
print(max(callory_sums))
print(callory_sums)
print(elf_meal_groups)
# Part 2
print("\nPart 2\n==================================\n")
copy_callory_sums = callory_sums
sum_top_3 = 0
for i in range(0,3):
    temp = max(copy_callory_sums)
    sum_top_3 = sum_top_3 + temp
    copy_callory_sums.remove(temp)
print(sum_top_3)
