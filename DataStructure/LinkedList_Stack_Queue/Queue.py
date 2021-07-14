# Queue(FIFO)
import sys, os
from .SinglyLinkedList import SinglyLinkedList

class Queue(object):
    lstInstance = SinglyLinkedList()
    def dequeue(self):
        return self.lstInstance.removeAt(0)
    def enqueue(self, value):
        return self.lstInstance.insertAt(value, self.lstInstance.getSize())
    
'''
queue = Queue()
queue.enqueue("a")
queue.lstInstance.printStatus()
queue.enqueue("b")
queue.lstInstance.printStatus()
queue.enqueue("c")
queue.lstInstance.printStatus()
queue.enqueue("d")
queue.lstInstance.printStatus()
queue.enqueue("e")
queue.lstInstance.printStatus()
queue.dequeue()
queue.lstInstance.printStatus()
queue.dequeue()
queue.lstInstance.printStatus()
queue.dequeue()
queue.lstInstance.printStatus()
queue.dequeue()
queue.lstInstance.printStatus()
queue.dequeue()
queue.lstInstance.printStatus()
'''