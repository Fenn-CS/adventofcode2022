# Problem statement: https://adventofcode.com/2022/day/7
from filesystem import Folder, File

rootFolder = Folder('/')
currentDir = rootFolder
with open('input', 'r') as input:
    for line in input:
        if line in ['\n', '\r\n']:
            pass # Thanks but, I would pass!
        else:
            print("Current directory is {}".format(currentDir.name))
            cliLine = line.strip('\n')
            if '$' in cliLine:
                command = cliLine.split()
                if len(command) == 3: # is cd
                    if command[2] == '..':
                        print(cliLine)
                        currentDir = currentDir.parent
                    else:
                        for directory in currentDir.children:
                            if directory.name == command[2]:
                                currentDir = directory
                    print("Moving to {}".format(currentDir.name))
                else: # is ls
                    pass
            elif 'dir' in cliLine:
                # It's a folder. Create it and add to the current directory
                folder = cliLine.split()
                folder = Folder(folder[1])
                currentDir.appendChild(folder)
            else:
                file = cliLine.split()
                file = File(file[1], file[0])
                currentDir.appendChild(file)

rootFolder.traverse(Folder.print) # print for nothing but the beauty

def checkSizeLessThan(node, size):
    node = node.get('item')
    if hasattr(node, 'getSize'):
        fSize = node.getSize()
        if fSize < size:
            return fSize
        return 0
    return 0

def checkSizeMaxes100k(node):
    return checkSizeLessThan(node, 100001)
_, max100kSizes, _ = rootFolder.traverse(checkSizeMaxes100k)
print(max100kSizes)
print(sum(max100kSizes))


# Part 2
sizeOfRoot = rootFolder.getSize()
freeSpace = 70000000 - sizeOfRoot
requiredSpace = 30000000 - freeSpace

print("Required space is {}".format(requiredSpace))
def checkAtLeast(node, size):
    node = node.get('item')
    if hasattr(node, 'getSize'):
        fSize = node.getSize()
        if fSize >= size and node.parent is not None:
            return fSize
        return 0
    return 0

def checkRequiredSpace(node):
    return checkAtLeast(node, requiredSpace)

_, hasEnoughSpace, _ = rootFolder.traverse(checkRequiredSpace)
hasEnoughSpace = list(filter(lambda x: x != 0, hasEnoughSpace))
print(hasEnoughSpace)
print(min(hasEnoughSpace))
