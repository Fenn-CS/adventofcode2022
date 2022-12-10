# Problem statement: https://adventofcode.com/2022/day/7
from __future__ import annotations

class File:
    def __init__(self, name, size: int):
        self.name = name
        self.size = int(size)

class Folder:
    def __init__(self, name, parent = None):
        self.name = name
        self.children = []
        self.parent = parent
    def appendChild(self, child: File | Folder):
        self.appendChildren([child])
    def appendChildren(self, children: [File | Folder]):
        for child in children:
            child.parent = self
            self.children.append(child)
    def traverse(self, applyOnNode = None, applyOnNodeList = None, level = 0):
        items = []
        applyOnNodeResults = []
        applyOnNodeListResult = None
        if self.parent is None:
            currentNode = {'level': level, 'item': self}
            items.append(currentNode)
            if applyOnNode is not None:
                applyOnNodeResults.append(applyOnNode(currentNode))
            level = level + 1
        for child in self.children:
            item = {'level':level, 'item':child}
            if applyOnNode is not None:
               applyOnNodeResults.append(applyOnNode(item))
            items.append(item)
            if isinstance(child, Folder):
                tempItems, tempApplyOnNodeResults, tempApplyOnNodeListResult = child.traverse(applyOnNode, applyOnNodeList, level + 1)
                items = items + tempItems
                applyOnNodeResults = applyOnNodeResults + tempApplyOnNodeResults
        if applyOnNodeList is not None:
            applyOnNodeListResult = applyOnNodeList(items)
        return items, applyOnNodeResults, applyOnNodeListResult
    def getSize(self):
        def checkSize(node):
            node = node.get('item')
            if hasattr(node, 'size'):
                return node.size
            return 0
        _, sizes, _ = self.traverse(checkSize)
        return sum(sizes)
    @staticmethod
    def print(item, addIndent = 2):
        indent = ' ' * item.get('level') * addIndent
        item = item.get('item')
        print("{}- {}".format(indent, item.name))

if __name__ == "__main__":
    rootFolder = Folder('root')
    pics = Folder('Pictures')
    downloads = Folder('Downloads')
    rootFolder.appendChildren([pics, downloads])
    gradPhotos = Folder('Graduation')
    travel = Folder('Travel')
    usTrip = Folder('US Trip')
    canadaTrip = Folder('Canada Trip')
    mexicoTrip = Folder('Mexico Trip')
    pics.appendChildren([gradPhotos, travel])
    travel.appendChildren([usTrip, canadaTrip, mexicoTrip])
    avast = File('Avast.exe', '500')
    dogPNG = File('American Bull.png', '1000')
    downloads.appendChildren([avast, dogPNG])
    folders = []
    print("Testing with sample folders and files")
    print("=====================================\n")
    print("Test tree\n=========\n")
    result, _, _ = rootFolder.traverse(Folder.print)
    print("\nAggregrate results from test tree")
    print("=================================\n")
    for item in result:
        level = item.get('level')
        item = item.get('item')
        print("{} is at level {}".format(item.name, level))
        if isinstance(item, Folder):
            print("Size of {} is {}".format(item.name, item.getSize()))
        print("------------------")
