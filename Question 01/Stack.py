import numpy

#create Stack Class
class Stack:
    def __init__(self, limit=10):
        self.limit = limit
        self.elements = numpy.array([0]*limit) #Fixed size numpy Array
        self.stack = 0

    #push data
    def push(self, data):
        if self.stack < self.limit: #Check If stack  < limit
            self.elements[self.stack] = data # Append data to Stack
            self.stack += 1

        else: #if Stack  > limit
            print("Stack Overflow")
            return
    #pop data
    def pop(self): #Delete returns a new Array also Retrieve last element before delete
        if self.stack == 0: #Check Stack equeal to '0'
            print("stack undrflow")
        else: # If Stack  Not Equal to '0'
            lastElement = self.elements [self.stack-1]# Delete the Last element
            self.stack -= 1
            return lastElement


    #Check Top Element in Stack
    def top(self):
        if self.stack == 0: #Check Stack  equeal to '0'
            print("stack undrflow")
        else:
            return self.elements[self.stack -1]

    # Check Stack is Empty
    def isEmptyStack(self):
        return self.size() == 0  # use function size

        # Check Stack is Full

    def isFullStack(self):
        return self.stack == self.limit

        # Check Stack Size

    def size(self):
        return self.stack
