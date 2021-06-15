from Stack import *
MyStack = Stack(10)
print("\n Top element is :" , MyStack.top())
print(" Is Stack is Empty :",MyStack.isEmptyStack())
print(" Number of Stack's elements :" , MyStack.size())
MyStack.push(10)
MyStack.push(20)
MyStack.push(30)
MyStack.push(40)
MyStack.push(50)
MyStack.push(60)
print(" Pop element is " , MyStack.pop())
MyStack.push(70)
MyStack.push(80)
print(" Number of Stack's elements :" , MyStack.size())
print(" Pop element is " , MyStack.pop())
print(" Top element is :" , MyStack.top())

print("\n** DISPLAY STACK **")
MyStack.printStack()
print("\nIs Stack is Empty :",MyStack.isEmptyStack())
print("Number of Stack's elements :" , MyStack.size())
print("Is Stack is Full :",MyStack.isFullStack())