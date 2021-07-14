'''
Singly linked list

Construct a singly linked list with nodes and references

A node consists of
    A variable to hold reference to its next node
    A variable to hold a reference to its value object
    
Head and Tail (not mandatory)
    Using them makes search, insert and delete more convenient.
    Head : Always at the first of the list.
    Tail : Always at the last of teh list.
    These are the two corner stone showing the start and the end of the list.
    
    index is starting after Headnode
''' 

class SinglyLinkedList:
    
    nodeHead = ''
    nodeTail = ''
    size = 0
    
    def __init__(self):
        self.nodeTail = Node(binTail =True)
        self.nodeHead = Node(binHead = True, nodeNext = self.nodeTail)
        
    def insertAt(self, objInsert, idxInsert):
        nodeNew = Node(objValue = objInsert)
        nodePrev = self.get(idxInsert -1)
        nodeNext = nodePrev.getNext()
        nodePrev.setNext(nodeNew)
        nodeNew.setNext(nodeNext)
        self.size = self.size + 1
    
    def removeAt(self, idxInsert):
        nodePrev = self.get(idxInsert -1)
        nodeRemove = nodePrev.getNext()
        nodeNext = nodePrev.getNext().getNext()
        nodePrev.setNext(nodeNext)
        self.size = self.size - 1
        return nodeRemove.getValue()
    
    def get(self, idxRetrieve):
        nodeReturn = self.nodeHead
        for idx in range(idxRetrieve+1):
            nodeReturn = nodeReturn.getNext()
        return nodeReturn
    
    def printStatus(self):
        idx = 0
        nodeCurrent = self.nodeHead
        while nodeCurrent.getNext().isTail() == False:
            nodeCurrent = nodeCurrent.getNext()
            if(nodeCurrent.getNext().isTail() == False):
                print("[", nodeCurrent.getValue(),",", idx, "]-", end='')
            else:
                print("[", nodeCurrent.getValue(),",", idx, "]", end='')
            idx += 1
        print()
    
    def getSize(self):
        return self.size
    


class Node:
    
    nodeNext = ''
    objValue = ''
    binHead = False
    binTail = False
    
    def __init__(self, objValue = '', nodeNext = '', binHead = False, binTail = False):
        self.nodeNext = nodeNext
        self.objValue = objValue
        self.binHead = binHead
        self.binTail = binTail
        
    def getValue(self):
        return self.objValue
    
    def getNext(self):
        return self.nodeNext
    
    def setValue(self, objValue):
        self.objValue = objValue
        
    def setNext(self, nodeNext):
        self.nodeNext = nodeNext
        
    def isHead(self):
        return self.binHead
    
    def isTail(self):
        return self.binTail

'''
list1 = SinglyLinkedList()
list1.insertAt('a',0)
list1.insertAt('b',1)
list1.insertAt('c',2)
list1.insertAt('d',3)
list1.insertAt('f',4)
list1.printStatus()

list1.insertAt('c',2)
list1.printStatus()

list1.removeAt(4)
list1.printStatus()
'''



