### chan 2019/12/27

## define a queue, FIFO
class Queue():
    def __init__(self, originQueue):
        self.items = originQueue
    
    def isEmpty(self):
        return self.items == []
    
    def enQueue(self, item):
        self.items.insert(0, item)

    def deQueue(self):
        self.items.pop()
    
    def size(self):
        return len(self.items)
    
if __name__ == "__main__":
    q = Queue([])
    q.enQueue(1)
    q.enQueue(2)
    print(q.size())
    q.deQueue()
    print(q.isEmpty())
    q.deQueue()
    print(q.isEmpty())

