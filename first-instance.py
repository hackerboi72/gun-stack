class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            print("Mag Is Empty")
            return None
        else:
            return self.stack.pop()  # Ensure you return the popped item

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)  # Fix redundant size method

    def display(self):
        if self.is_empty():
            print("Empty Mag")
        else:
            print("Mag:", self.stack)

# Testing the stack
clip = Stack()
clip.push(1)
clip.push(2)
clip.pop()
clip.pop()
clip.display()
