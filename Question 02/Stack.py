# Class Create a node of linked list and allocate memory to it
class Node:
    # constructor
    def __init__(self):
        self.data = None
        self.Next = None

    # set data of the node
    def setData(self , data):
        self.data = data

    # get data of the node
    def getData(self):
        return self.data

    # set next of the data
    def setNext(self ,address):
        self.Next = address

    # get data of this node
    def getNext(self):
        return self.Next

#Create the Stack Class
class Stack:
    def __init__(self, limit=10):
        self.limit = limit
        self.head = Node()
        self.stack = []
    # Putting a new element
    def push(self, data):
        # create the new node
        newNode = Node()
        newNode.setData(data)

        if len(self.stack) < self.limit:  # Check If stack length < limit
            if self.head is None:  # Check linked list head is NULL
                self.head = newNode  # Assign head to newNode
            else:
                newNode.setData(data)
                newNode.setNext(self.head)
                self.head = newNode
            return self.stack.append(data)  # Append data to Stack
        else:
            print("Stack Overflow")
            return
    # Remove element that is in the current head
    def pop(self):
        if self.head is None:
            print(" stack underflow")
            return
        else:
            # Removes the head node and makes the preceeding one the new head
            poppednode = self.head
            self.head = self.head.getNext()
            poppednode.getNext = None
            poppednode.data
            return self.stack.pop()

    # Return the head node data
    def top(self):
        if self.head is None:  # Check linked list head is none
            print("\n Stack underflow")
            return
        else:
            return self.head.data
            return self.stack[len(self.stack) - 1]

    # Check Stack is Empty
    def isEmptyStack(self):
        if len(self.stack) == 0:  # Check Stack length equeal to '0'
            return True
        else:
            return False

    # Check Stack is Full
    def isFullStack(self):
        if len(self.stack) == self.limit:
            return True
        else:
            return False

    # Check Stack Size
    def size(self):
        return len(self.stack)

    # Print out the Stack
    def printStack(self):
        current = self.head
        if self.isEmptyStack():
            print("Stack underflow")
        else:
           while current is not None:
                print(current.getData(), "->", end=" ")
                current = current.getNext()

