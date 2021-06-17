from Stack import Stack

myStack = Stack(8)

print("\nIs Stack Empty ? : ", myStack.isEmptyStack())
print("Stack size :" , myStack.size())
myStack.push(10)
myStack.push(20)
myStack.push(30)
print("Stack Top element is :" , myStack.top())
myStack.push(40)
myStack.push(50)
myStack.push(60)
print("Stack Pop Element is :" ,myStack.pop())# Remove the last element in stack

print("Stack Top element is :" , myStack.top())
print("Stack size :" , myStack.size())
print("Is Stack Full ? : " , myStack.isFullStack())


