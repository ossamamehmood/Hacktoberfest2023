class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            return self.stack.pop()

    def peek(self):
        if not self.is_empty():
            print("Stack is empty.")
        else:
            return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)
    

stack = Stack()
n = int(input("Enter the maximum number of inputs: "))

while True:
    print("Stack Menu:")
    print("1. Push")                            #push item into stack
    print("2. Pop")                             #pop item from stack
    print("3. Peek")                            #peek at the top item
    print("4. Check if stack is empty")         
    print("5. Get stack size")
    print("0. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        if len(stack.stack) < n:
            item = input("Enter item to push: ")
            stack.push(item)
        else:
            print("Cannot push item. Stack is full.")
    elif choice == "2":
        popped_item = stack.pop()
        if popped_item:
            print("Popped item: ", popped_item)
    elif choice == "3":
        top_item = stack.peek()
        if top_item:
            print("Top item: ", top_item)
    elif choice == "4":
        if stack.is_empty():
            print("Stack is empty.")
        else:
            print("Stack is not empty.")
    elif choice == "5":
        print("Size of stack:", stack.size())
    elif choice == "0":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")