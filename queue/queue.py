"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         self.storage.append(value)
#         self.size +=1

#     def dequeue(self):
#         if self.size > 0:
#             item = self.storage.pop(0)
#             self.size -=1
#             return item
#         else:
#             return None

class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

class Queue:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        newNode = Node(value)
        self.size +=1

        if not self.head and not self.tail:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next_node = newNode
            self.tail = newNode

    def dequeue(self):
        if not self.head:
            return None
        elif self.head.next_node is None:
            self.size -= 1
            item = self.head.value
            self.head = None
            self.tail = None
            return item
        else:
            self.size -= 1
            item = self.head.value
            self.head = self.head.next_node
            return item
