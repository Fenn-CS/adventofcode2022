# Problem statement: https://adventofcode.com/2022/day/4
groups = []
faulty_groups = []
with open('input', 'r') as input:
    for line in input:
        if line in ['\n', '\r\n']:
            pass
        else:
            pair = line.strip()
            pair = pair.split(',')
            first_group_section = pair[0].split('-')
            first_group_section = list(map(lambda x: int(x), first_group_section))
            second_group_section = pair[1].split('-')
            second_group_section = list(map(lambda x: int(x), second_group_section))
            groups.append([first_group_section, second_group_section])
for group in groups:
    a_range = range(group[0][0], group[0][1]+1)
    b_range = range(group[1][0], group[1][1]+1)
    if (group[0][0] in b_range or group[0][1] in b_range) or (group[1][0] in a_range or group[1][1] in  a_range):
        faulty_groups.append(group)

print(len(faulty_groups))
