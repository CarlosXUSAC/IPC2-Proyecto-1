from dataclasses import dataclass


@dataclass
class Node:
    value: int
    nextNode: 'Node'


class LinkedList:
    _size: int
    _firstNode: Node

    def __init__(self) -> None:
        self._size = 0
        self._firstNode = None

    def add(self, position: int, element: int):
        if position == 0:
            self._firstNode = Node(value=element, nextNode=self._firstNode)

        else:
            currentNode = self._firstNode
            for _ in range(0, position - 1):
                currentNode = currentNode.nextNode
            currentNode.nextNode = Node(
                value=element, nextNode=currentNode.nextNode)

        self._size += 1

    def delete(self, position: int):
        if position == 0:
            self._firstNode = self._firstNode.nextNode

        else:
            currentNode = self._firstNode
            for _ in range(0, position - 1):
                currentNode = currentNode.nextNode
            currentNode.nextNode = currentNode.nextNode.nextNode

        self._size -= 1

    def get(self, position: int) -> int:
        currentNode = self._firstNode
        for _ in range(0, position):
            currentNode = currentNode.nextNode
        return currentNode.value

    def getSize(self) -> int:
        return self._size


example = LinkedList()
example.add(0, 1)
print(example.getSize())
