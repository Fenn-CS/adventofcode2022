# Problem statement: https://adventofcode.com/2022/day/3
import string
alpha_lowercase = dict(zip(string.ascii_lowercase, range(1,27)))
alpha_uppercase = dict(zip(string.ascii_uppercase, range(27,53)))
ruckstack_groups = []
temp_group = []
group_symbols = []
line_count = 0
with open('input_2', 'r') as input:
    for line in input:
        ruckstack = [*line.strip()]
        temp_group.append(ruckstack)
        line_count = line_count + 1
        if line_count % 3 == 0:
            ruckstack_groups.append(temp_group)
            temp_group = []
for group in ruckstack_groups:
    if len(group) != 3:
        raise Exception("Group not right!")
    found_in_group = False
    for elf_compartment in group:
        if found_in_group:
            break
        for item in elf_compartment:
            if item in group[0] and item in group[1] and item in group[2]:
                found_in_group = True
                if item.islower():
                    group_symbols.append(alpha_lowercase.get(item))
                    break
                else:
                    group_symbols.append(alpha_uppercase.get(item))
                    break

if len(group_symbols) != len(ruckstack_groups):
    raise Exception("Group symbol count and group count don't match")
print(sum(group_symbols))
