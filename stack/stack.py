"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.size+=1
#         self.storage.append(value)

#     def pop(self):
#         if len(self.storage) > 0:
#             self.size -=1
#             item = self.storage.pop(-1)
#             return item
#         else:
#             return None


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class Stack:

    def __init__(self):
        self.size = 0
        self.tail = None
        self.head = None

    def __len__(self):
        return self.size
    
    def push(self, value):
        newNode = Node(value)
        self.size +=1

        if not self.head and not self.tail:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
    
    def pop(self):
        if not self.head:
            return None
        elif self.head.next is None:
            self.size -=1
            item = self.head.value
            self.head = None
            return item
        else:
            self.size -=1
            item = self.tail.value
            cur = self.head

            while cur.next != None:
                if cur.next == self.tail:
                    self.tail = cur
                    cur.next = None
                    break
                cur = cur.next
            return item
