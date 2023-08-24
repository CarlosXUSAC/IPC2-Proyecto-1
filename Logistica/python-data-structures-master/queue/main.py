from dataclasses import dataclass


@dataclass
class Node:
    value: int
    nextNode: 'Node'


class Queue:
    _size: int
    _firstNode: Node
    _lastNode: Node

    def __init__(self) -> None:
        self._size = 0
        self._firstNode = None
        self._lastNode = None

    def add(self, element: int):
        newNode = Node( value=element, nextNode=None)

        if self._size == 0:
            self._firstNode = newNode
        else:
            self._lastNode.nextNode = newNode

        self._lastNode = newNode
        self._size += 1

    def delete(self):
        self._firstNode = self._firstNode.nextNode
        self._size -= 1

    def get(self) -> int:
        return self._firstNode.value

    def getSize(self) -> int:
        return self._size


myStack = Queue()
myStack.add(1)
myStack.add(2)
myStack.delete()
print(myStack.getSize())
