class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

    def size(self):
        return len(self.items)

if __name__ == "__main__":
    stack = Stack()

    print("Is the stack empty?", stack.is_empty())

    stack.push(1)
    stack.push(2)
    stack.push(3)

    print("Stack after pushing 1, 2, and 3:", stack.items)

    popped_item = stack.pop()
    print("Popped item:", popped_item)

    print("Stack after popping:", stack.items)

    top_item = stack.peek()
    print("Top item:", top_item)

    print("Stack size:", stack.size())
