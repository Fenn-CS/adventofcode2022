# Problem statement: https://adventofcode.com/2022/day/5
stacks = []
moveAlgo = []
numberOfStacksKnown = False
numberOfStacks = 0
with open('input', 'r') as input:
    for line in input:
        if (('1' in line) and not ('m' in line)) or line in ['\n', '\r\n']: # The input contains the number stacks at the end, quite crazy!
            continue
        if 'm' in line:
            instruction = line.strip()
            instruction = instruction.split(' ')
            algo = {}
            algo['move'] = int(instruction[1])
            algo['from'] = int(instruction[3])
            algo['to'] = int(instruction[5])
            moveAlgo.append(algo)
        else:
            rawCrateInputs = line
            rawCrateInputs = rawCrateInputs.replace(' ', '?')
            currentCrates = []
            i = 1
            lengthOfRawCrateInputs = len(rawCrateInputs)
            currentCrates.append(rawCrateInputs[i])
            while i <= lengthOfRawCrateInputs:
                i = i + 2
                if i < lengthOfRawCrateInputs:
                    currentCrates.append(rawCrateInputs[i])
            currentCrates.pop()
            nonSpacedCrates = []
            for i in range(0, len(currentCrates)):
                if i % 2 == 0:
                    nonSpacedCrates.append(currentCrates[i])
            # print(nonSpacedCrates)
            currentCrates = nonSpacedCrates
            lengthOfCurrentCrates = len(currentCrates)
            temp = ['None'] * lengthOfCurrentCrates
            for i in range(0, lengthOfCurrentCrates):
                if currentCrates[i] != '?':
                    temp[i] = currentCrates[i]
            # print(temp)
            currentCrates = temp
            if not numberOfStacksKnown:
                numberOfStacks = lengthOfCurrentCrates
                numberOfStacksKnown = True
                from collections import deque
                for i in range(0, numberOfStacks):
                    stacks.append(deque())
            for j in range(0, numberOfStacks):
                stacks[j].appendleft(currentCrates[j])
    
# This is absolutely crazy
# I spent 4 hours! Yes 4 hours trying to get the input organized in a useful and non-hacky way
# I mean a way that could work for any number of crates
# I feel like this problem is to test string manipulation or data extraction or WHAT? (YELLS)
# Well now let's solve the actual problem
# ===========================

# Remove spaces on top so that, they are not moved as crates
for stack in stacks:
    while stack[-1] == 'None':
        stack.pop()
for instruction in moveAlgo:
    move = int(instruction.get('move'))
    fromStack = int(instruction.get('from')) - 1 # counting starts from 0, tell you children!
    to = instruction.get('to') - 1
    for i in range(0, move):
        # print(move, fromStack, to) (optional print out to see moves)
        if stacks[fromStack]:
            crateInHand = stacks[fromStack].pop()
            stacks[to].append(crateInHand)
        # print(stacks) (optional print out to see state of stacks after each move)
code = ''
for stack in stacks:
    if stack and stack[-1] != 'None':
        code = code + stack[-1]
print(code)

