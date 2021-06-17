import numpy

#create Stack Class
class Stack:
    def __init__(self, limit=10):
        self.limit = limit
        self.elements = numpy.array([0]*limit) #Fixed size numpy Array
        self.stack = 0

    #push data (Input an element to the top of numpy Array)
    def push(self, data):
        if self.stack < self.limit : # If the Stack is not full for the giving limit
            self.elements[self.stack] = data # Add new element to the Stack
            self.stack += 1 # Increse the Stack size

        else: # If Stack is full
            print("Stack Overflow")
            return


    #pop data (Remove the topmost element from the stack)
    def pop(self): # Delete returns a new Array also Retrieve last element before delete
        if self.stack == 0: # Check Stack equeal to '0'
            print("stack undrflow")  # Stack is Empty

        else: # If Stack  Not Equal to '0'
            lastElement=self.elements[self.stack -1 ] # If Stack is not empty ,get the element which is pointing at the top of the Stack.
            self.stack -= 1  # Decrease the size of the Stack by 1
            return lastElement  # Return last element in Stack


    #Check Top Element in Stack
    def top(self):
        if self.stack == 0: #Check Stack equeal to '0'
            print("stack undrflow") # The Stack is Empty
        else: # If Stack is not Empty
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

