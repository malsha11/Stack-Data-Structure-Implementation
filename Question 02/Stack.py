# Class Create a node of linked list
class Node:
    # constructor
    def __init__(self):
        self.data = None
        self.Next = None

    # set data of the node
    def setData(self, data):
        self.data = data

    # get data of the node
    def getData(self):
        return self.data

    # set next of the data
    def setNext(self, address):
        self.Next = address

    # get data of this node
    def getNext(self):
        return self.Next

class Stack:
    def __init__(self, limit=10):
        self.limit = limit
        self.head = Node()
        self.stack = []

    def push(self, data):
        # create the new node
        newNode = Node()
        newNode.setData(data)

        if len(self.stack) < self.limit: #Check If stack length < limit
            if self.head is None: #Check linked list head is none
                self.head = newNode #Assign head to newNode
            else:
                newNode.setData(data)
                newNode.setNext(self.head)
                self.head = newNode
            return self.stack.append(data) # Append data to Stack
        else:
            print("Stack Overflow")
            return
