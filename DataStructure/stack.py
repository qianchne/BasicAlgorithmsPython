### chan 2019/12/27


## define a stack, FILO
class stack:
    def __init__(self, originStack):
        self.items = originStack     
        self.message = ''
    
    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()
        if len(self.items) == 0:
            self.message = 'Warring: the stack is empty'
            print(self.message)
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
    
    def printStack(self):
        print(self.items)



if __name__ == "__main__":
    s = stack([1,2])
    s.pop()
    s.pop()
    #s.pop()
    s.push(1)
    print(s.size())
    s.printStack()
    print(s.isEmpty())