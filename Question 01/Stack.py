import numpy

#create Stack Class
class Stack:
    def __init__(self, limit=10):
        self.limit = limit
        self.elements = numpy.array([0]*limit) #Fixed size numpy Array
        self.stack = 0

    #push data
    def push(self, data):
        if self.stack< self.limit : #check If Stack < limit
            self.elements[self.stack] = data # Append data to Stack
            self.stack += 1 # stack = Stack+1


        else: #if Stack  > limit
            print("Stack Overflow")
            return


    #pop data
    def pop(self): # Delete returns a new Array also Retrieve last element before delete
        if self.stack == 0: # Check Stack equeal to '0'
            print("stack undrflow")  # Stack is Empty

        else: # If Stack  Not Equal to '0'
            lastElement=self.elements[self.stack -1 ] # delete the last element
            self.stack -= 1  # stack = stack -1
            return lastElement  # get last element in Stack


    #Check Top Element in Stack
    def top(self):
        if self.stack == 0: #Check Stack equeal to '0'
            print("stack undrflow")
        else:
            return self.elements[self.stack -1] # Return the top element in stack


    # Check if the stack is Empty
    def isEmptyStack(self):
        return self.size() == 0  # use function size

    # Check if the stack is Full
    def isFullStack(self):
        return self.stack == self.limit #if stack size  == limit --It is a Full Stack (stack Overflow)

    # Check Stack Size

    def size(self):
        return self.stack
