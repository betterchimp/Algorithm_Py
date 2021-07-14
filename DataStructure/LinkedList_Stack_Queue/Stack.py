# Stack(LIFO)
# https://dojang.io/mod/page/view.php?id=2450 (import 관련 사이트_)
from SinglyLinkedList import *

class Stack(object):
    lstInstance = SinglyLinkedList()
    def pop(self):
        return self.lstInstance.removeAt(0)
    def push(self, value):
        return self.lstInstance.insertAt(value, 0)

stack = Stack()
stack.push("a")
stack.lstInstance.printStatus()
stack.push("b")
stack.lstInstance.printStatus()
stack.push("c")
stack.lstInstance.printStatus()
stack.pop()
stack.lstInstance.printStatus()
stack.pop()
stack.lstInstance.printStatus()
stack.pop()
stack.lstInstance.printStatus()