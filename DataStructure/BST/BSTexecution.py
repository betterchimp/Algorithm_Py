from BinarySearchTree import BinarySearchTree
import sys

B = BinarySearchTree()

while(True):
    print("enter op and val(mode) seperately")
    op = sys.stdin.readline().rstrip()
    val = int(sys.stdin.readline())
    if op == "i":
        B.insert(val)
        B.traverse()
    if op == "d":
        B.delete(val)
        B.traverse()
    if op == "s":
        print(B.search(val))
        B.traverse()
    if op == "t":
        B.traverse(val)
    if op == "q":
        print("Bye")
        break