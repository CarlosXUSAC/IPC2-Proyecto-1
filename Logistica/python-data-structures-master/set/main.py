from dataclasses import dataclass


@dataclass
class Node:
    value: int
    nextNode: 'Node'


class Set:
    _size: int
    _firstNode: Node

    def __init__(self) -> None:
        self._size = 0
        self._firstNode = None

    def add(self, element: int):
        if not self.contains(element):
            self._firstNode = Node(
                value=element,
                nextNode=self._firstNode
            )

    def delete(self, element: int):
        if self._firstNode.value == element:
            self._firstNode = self._firstNode.nextNode
            self._size -= 1
        else:
            currentNode = self._firstNode
            while currentNode.nextNode.value != element:
                currentNode = currentNode.nextNode
                if currentNode.nextNode == None:
                    return
            currentNode.nextNode = (
                currentNode.nextNode.nextNode
            )
            self._size -= 1

    def contains(self, element: int) -> bool:
        currentNode = self._firstNode
        while currentNode != None:
            if currentNode.value == element:
                return True
            currentNode = currentNode.nextNode
        return False

    def getSize(self) -> int:
        return self._size


example = Set()
example.add(1)
example.add(4)
print(example.contains(1)) # True
print(example.contains(3)) # False
print(example.getSize()) # 2
