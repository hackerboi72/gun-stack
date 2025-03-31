
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
            return self.stack.pop()  

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)  

    def display(self):
        if self.is_empty():
            print("Empty Mag")
        else:
            print("Mag:", self.stack)


clip = Stack()
for i in range(1,18): #Change the number after the comma to adjust the number of bullets stored in the magazine 
    clip.push(i)
    clip.size()
    clip.display()
    print("Shoot the Gun")

for i in range(3): #Change this number to adjust how many bullets you want to shoot 
    clip.pop()
clip.size()
clip.display()
