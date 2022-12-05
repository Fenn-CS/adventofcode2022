# Problem statement: https://adventofcode.com/2022/day/3
import string
alpha_lowercase = dict(zip(string.ascii_lowercase, range(1,27)))
alpha_uppercase = dict(zip(string.ascii_uppercase, range(27,53)))
ruckstacks = []
odd_ruckstack_items = []
with open('input', 'r') as input:
    for line in input:
        if line in ['\n', '\r\n']:
            pass
        else:
            ruckstack = [*line.strip()]
            ruckstacks.append(ruckstack)
            first_half = ruckstack[:len(ruckstack)//2]
            second_half = ruckstack[len(ruckstack)//2:]
            for i in range(0, len(first_half)):
                if first_half[i] in second_half:
                    if first_half[i].islower():
                        odd_ruckstack_items.append(alpha_lowercase.get(first_half[i]))
                        break
                    else:
                        odd_ruckstack_items.append(alpha_uppercase.get(first_half[i]))
                        break

# Part 1
if len(ruckstacks) == len(odd_ruckstack_items):
    print(sum(odd_ruckstack_items))
else:
    print("Something is wrong!")
