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
    


