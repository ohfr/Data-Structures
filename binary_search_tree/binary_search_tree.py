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

        # qe = Queue()

        # qe.enqueue(node)
        # while qe.size is not 0:
        #     cur = qe.dequeue()
        #     print(cur)
        #     if cur.left:
        #         qe.enqueue(cur.left)
        #     if cur.right:
        #         qe.enqueue(cur.right)
        q = []

        q.append(node)

        while q:
            cur = q.pop(0)
            print(cur.value)
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

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

        stack = []

        stack.append(node)

        while stack:
            cur = stack.pop(-1)
            print(cur.value)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

