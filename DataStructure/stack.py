### chan 2019/12/27


## define a stack, FILO
class stack:
    def __init__(self):
        self.items = []   
        self.message = ''
    
    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items)-1 >= 0 :
            self.items.pop()
        else :
            print('stack is empty')
    
    def peek(self):
        if len(self.items)-1 >= 0 :
            return self.items[len(self.items)-1]
        else :
            print('stack is empty')
    
    def size(self):
        return len(self.items)
    
    def printStack(self):
        print(self.items)



if __name__ == "__main__":
    s = stack()
    s.push(1)
    s.push(2)
    s.pop()
    s.pop()
    #s.pop()
    s.push(1)
    print(s.size())
    s.printStack()
    print(s.isEmpty())