"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None # Stores a node, that corresponds to our first node in the list 
        self.tail = None # stores a node that is the end of the list
    
    def add_to_head(self, value):
        # create a node to add
        new_node = Node(value)
        # check if list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # new_node should point to current head
            new_node.next_node = self.head
            # move head to new node
            self.head = new_node

    def add_to_tail(self, value):
        # create a node to add
        new_node = Node(value)
        # check if list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # point the node at the current tail, to the new node
            self.tail.next_node = new_node
            self.tail = new_node

    # remove the head and return its value
    def remove_head(self):
        # if list is empty, do nothing
        if not self.head:
            return None
        # if list only has one element, set head and tail to None
        if self.head.next_node is None:
            head_value = self.head.value
            self.head = None
            self.tail = None
            return head_value
        # otherwise we have more elements in the list
        head_value = self.head.value
        self.head = self.head.next_node
        return head_value 

    def contains(self, value):
        if self.head is None:
            return False
        
        # Loop through each node, until we see the value, or we cannot go further
        current_node = self.head

        while current_node is not None:
        # check if this is the node we are looking for
            if current_node.value == value:
                return True

            # otherwise, go to the next node
            current_node = current_node.next_node
        return False 

    def get_max(self):
        if self.head:
            cur = self.head
            greatest = 0

            while cur != None:
                if cur.value > greatest:
                    greatest = cur.value
                cur = cur.next_node
            return greatest
        else:
            return None

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
       self.size += 1
       self.storage.add_to_tail(value)

    def dequeue(self):
        if self.size == 0:
            return None
        
        self.size -=1
        val = self.storage.remove_head()
        return val

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size
    
    def push(self, value):
        self.size +=1
        self.storage.add_to_head(value)

    def pop(self):
        if self.size == 0:
            return None
        self.size -=1
        item = self.storage.remove_head()
        return item


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # take current value of our node (self.value)
        # compare to new value we want to insert


        # if new value < self.value
            # set the left to the new value

        # if new value >= self.value
            # set right child to new value


        if value < self.value:
            if self.left:
                return self.left.insert(value)
            else:
                self.left = BSTNode(value)
        else:
            if self.right:
                return self.right.insert(value)
            else:
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True

        if target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        else:
            if self.right:
                return self.right.contains(target)
            else:
                return False


    # Return the maximum value found in the tree
    def get_max(self):
        # non recursive

        # curMax = self.value

        # cur = self

        # while cur != None:
        #     if cur.value > curMax:
        #         curMax = cur.value
        #     cur = cur.right
        # return curMax

        # recursive

        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # fn(self.value)
        
        # if self.left:
        #     self.left.for_each(fn)
        
        # if self.right:
        #     self.right.for_each(fn)
        

        # in order version!
        if self.left:
            self.left.for_each(fn)

        fn(self.value)

        if self.right:
            self.right.for_each(fn)
        

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        self.for_each(print)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # create a queue for nodes
        # add first node to queue
        # while queue is not empy
            # remove first node from the queue
            # print removed node
            # add all children to queue

        # q = []

        # q.append(node)

        # while q:
        #     cur = q.pop(0)
        #     print(cur.value)
        #     if cur.left:
        #         q.append(cur.left)
        #     if cur.right:
        #         q.append(cur.right)
        q = Queue()

        q.enqueue(node)

        while q:
            cur = q.dequeue()

            print(cur.value)

            if cur.left:
                q.enqueue(cur.left)
            if cur.right:
                q.enqueue(cur.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass
        # create stack
        # add first node to stack
        # while stack is not empty
        # get current node from top of stack
        # print node
        # add all children of node to stack
        # ORDER OF CHILDREN WILL MATTER

        # stack = []

        # stack.append(node)

        # while stack:
        #     cur = stack.pop(-1)
        #     print(cur.value)
        #     if cur.left:
        #         stack.append(cur.left)
        #     if cur.right:
        #         stack.append(cur.right)

        s = Stack()

        s.push(node)

        while s:
            cur = s.pop()
            print(cur.value)
            if cur.left:
                s.push(cur.left)
            if cur.right:
                s.push(cur.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)

        if node.left:
            node.left.pre_order_dft(node.left)
        if node.right:
            node.right.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node.left:
            node.left.post_order_dft(node.left)

        if node.right:
            node.right.post_order_dft(node.right)

        print(node.value)


