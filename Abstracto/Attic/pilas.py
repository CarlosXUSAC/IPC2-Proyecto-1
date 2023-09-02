from dataclasses import dataclass


@dataclass
class Node:
    value: int
    nextNode: 'Node'


class Stack:
    _size: int
    _firstNode: Node

    def __init__(self) -> None:
        self._size = 0
        self._firstNode = None

    def add(self, element: int):
        self._firstNode = Node(
            value=element,
            nextNode=self._firstNode
        )
        self._size += 1

    def delete(self):
        self._firstNode = self._firstNode.nextNode
        self._size -= 1

    def get(self) -> int:
        return self._firstNode.value

    def getSize(self) -> int:
        return self._size


myStack = Stack()
myStack.add(1)
myStack.add(2)
myStack.delete()
print(myStack.getSize())