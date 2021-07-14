import sys, os
from collections import deque

class TreeNode:
    nodeLHS = ""
    nodeRHS = ""
    nodeParent = ""
    value = ""

    def __init__(self, value, nodeParent):
        self.value = value
        self.nodeParent = nodeParent

    def getLHS(self):
        return self.nodeLHS

    def getRHS(self):
        return self.nodeRHS

    def getValue(self):
        return self.value

    def getParent(self):
        return self.nodeParent

    def setLHS(self, LHS):
        self.nodeLHS = LHS

    def setRHS(self, RHS):
        self.nodeRHS = RHS

    def setValue(self, value):
        self.value - value

    def setParent(self, nodeParent):
        self.nodeParent = nodeParent

class BinarySearchTree:
    root = ""
    count = 0
    
    def __init__(self):
        pass

    def insert(self, value, node = ""):
        if self.root == "":
            self.root = TreeNode(value, "")
            return
        
        if node == "":
            node = self.root

        if value == node.getValue():
            return

        if value > node.getValue():
            if node.getRHS() == "":
                node.setRHS(TreeNode(value, node))
            else:
                self.insert(value, node.getRHS())
            return

        if value < node.getValue():
            if node.getLHS() == "":
                node.setLHS(TreeNode(value, node))
            else:
                self.insert(value, node.getLHS())
            return

    def search(self, value, node = ""):

        if node == "":
            node = self.root

        if value == node.getValue():
            return True

        if value > node.getValue():
            if node.getRHS() == "":
                return False
            else:
                return self.search(value, node.getRHS())

        if value < node.getValue():
            if node.getLHS() == "":
                return False
            else:
                return self.search(value, node.getLHS())

    def findMax(self, node = ""):

        if node == "":
            node = self.root

        if node.getRHS() == "":
            return node

        return self.findMax(node.getRHS())


    def findMin(self, node = ""):

        if node == "":
            node = self.root

        if node.getLHS() == "":
            return node

        return self.findMin(node.getLHS())


    def delete(self, value, node = ""):

        if node == "":
            node = self.root

        if node.getValue() > value:
            self.delete(value, node.getLHS())

        elif node.getValue() < value:
            self.delete(value, node.getRHS())

        elif node.getValue() == value:

            if node.getLHS() != "" and node.getRHS() != "":
                nodeMax = self.findMax(node.getRHS())
                node.setValue(nodeMax.getValue())
                self.delete(nodeMax.getValue(), nodeMax)
                return

            parent = node.getParent()
            if node.getLHS() != "":
                if node == self.root:
                    self.root = node.getLHS()
                elif parent.getValue() > node.getValue():
                    parent.setLHS(node.getLHS())
                    node.getLHS().setParent(parent)
                else:
                    parent.setRHS(node.getLHS())
                    node.getLHS().setParent(parent)
                return

            if node.getRHS() != "":
                if node == self.root:
                    self.root = node.getRHS()
                elif parent.getValue() > node.getValue():
                    parent.setLHS(node.getRHS())
                    node.getRHS().setParent(parent)
                else:
                    parent.setRHS(node.getRHS())
                    node.getRHS().setParent(parent)
                return

            if node == self.root:
                self.root = ""
            elif parent.getValue() > node.getValue():
                parent.setLHS("")
            else:
                parent.setRHS("")
            return

        else:
            return False


#DFT(Depth First Traverse)


    def traverseInOrder(self, node = ""):
        if node == "":
            node = self.root
        ret = []
        if node.getLHS() != "":
            ret = ret + self.traverseInOrder(node.getLHS())
        ret.append(node.getValue())
        if node.getRHS() != "":
            ret = ret + self.traverseInOrder(node.getRHS())
        return ret


    def traversePreOrder(self, node = ""):
        if node == "":
            node = self.root
        ret = []
        ret.append(node.getValue())
        if node.getLHS() != "":
            ret = ret + self.traversePreOrder(node.getLHS())
        if node.getRHS() != "":
            ret = ret + self.traversePreOrder(node.getRHS())
        return ret


    def traversePostOrder(self, node = ""):
        if node == "":
            node = self.root
        ret = []
        if node.getLHS() != "":
            ret = ret + self.traversePostOrder(node.getLHS())
        if node.getRHS() != "":
            ret = ret + self.traversePostOrder(node.getRHS())
        ret.append(node.getValue())
        return ret


#BFT(Breadth First Traverse)


    def traverseLevelOrder(self):
        ret = []
        Q = deque()
        Q.append(self.root)
        while Q.isEmpty() == False:
            node = Q.popleft()
            if node == "":
                continue
            ret.append(node.getValue())
            if node.getLHS() != "":
                Q.append(node.getLHS())
            if node.getRHS() != "":
                Q.append(node.getRHS())
        return ret

    
    def traverse(self, mode = ""):
        if mode == "in" or mode =="":
            print(self.traverseInOrder())
        elif mode == "pre":
            print(self.traversePreOrder())
        elif mode == "post":
            print(self.traversePostOrder())
        elif mode == "level":
            print(self.traverseLevelOrder())
            

