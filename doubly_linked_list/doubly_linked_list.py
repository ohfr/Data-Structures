"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        self.length +=1
        newNode = ListNode(value)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode



    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        if self.head:
            if self.head != self.tail:

                self.length -= 1
                item = self.head.value
                nextNode = self.head.next
                nextNode.prev = None
                self.head.next = nextNode.next
                self.head = nextNode
                return item
            else:
                self.length -=1
                item = self.head.value
                self.head.delete()
                self.tail.delete()
                self.head = None
                self.tail = None
                return item
        else:
            return None
        

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        self.length +=1
        if self.tail:
            self.tail.insert_after(value)
            self.tail = self.tail.next
        else:
            newNode = ListNode(value)
            self.head = newNode
            self.tail = newNode

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        if self.tail:
            if self.tail != self.head:

                self.length -=1
                item = self.tail.value
                prev = self.tail.prev
                prev.next = None
                self.tail.prev = prev.prev
                self.tail = prev
                return item
            else:
                self.length -=1
                item = self.tail.value
                self.tail.delete()
                self.head.delete()                
                self.head = None
                self.tail = None
                return item
        else:
            return None


    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        if self.head:
            if self.head != self.tail:
                if node == self.tail:
                    self.remove_from_tail()

                    node.prev = None
                    node.next = self.head
                    self.head.prev = node
                    self.head = node
                    self.length +=1
                else:
                    prev = node.prev
                    nextNode = node.next
                    
                    nextNode.prev = prev
                    prev.next = nextNode

                    self.head.prev = node
                    node.next = self.head
                    node.prev = None
                    self.head = node
            else:
                return
        else:
            self.length +=1
            self.head = node
            self.tail = node

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if self.tail:
            if self.tail != self.head:
                if node == self.head:
                    self.remove_from_head()

                    node.next = None
                    self.tail.next = node
                    node.prev = self.tail
                    self.tail = node
                    self.length +=1
                else:
                    prev = node.prev
                    nextNode = node.next
                    
                    nextNode.prev = prev
                    prev.next = nextNode

                    self.tail.next = node
                    node.prev = self.tail
                    self.tail = node
                    self.tail.next = None
        else:
            self.length +=1
            self.head = node
            self.tail = node

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        if node == self.head:
            self.remove_from_head()
        elif node == self.tail:
            self.remove_from_tail()
        else:
            prev = node.prev
            nextNode = node.next
            prev.next = node.next
            nextNode.prev = prev
            node.delete()
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        currentMax = 0
        curNode = self.head

        while curNode is not None:
            if curNode.value > currentMax:
                currentMax = curNode.value
            curNode = curNode.next
        return currentMax