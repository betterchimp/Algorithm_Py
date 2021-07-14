'''
In Python, List is an Array.

Each element is accessible by index.

Problems in Array
    Whenever you put something in or get something out,
    you have to perform line-wise retrievals (N retrievals)

Linked list can overcome the line-wise retrievals.
'''

x = ['a', 'b', 'd', 'e', 'f']
print("x : ", x)

#Array insert
insert_idx = 2
insert_val = 'c'

y= list(range(6))
for idx in range(0, insert_idx):
    y[idx] = x[idx]
y[insert_idx] = insert_val
for idx in range(insert_idx, len(x)):
    y[idx+1] = x[idx]
x=y
print("x :", x)

#Array delete
delete_idx = 2

y= list(range(5))
for idx in range(0, delete_idx):
    y[idx] = x[idx]
for idx in range(delete_idx, len(y)):
    y[idx] = x[idx+1]
x=y
print("x :", x)