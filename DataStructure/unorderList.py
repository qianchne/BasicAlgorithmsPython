### chan 2019/12/27
## unordered list

## 构建节点类
class node():
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
    def getData(self):
        return self.data

    def setData(self, newdata):
        self.data = newdata
    
    def getNext(self):
        return self.next

    def setNext(self, newNext):
        self.next = newNext

## 利用节点类，构建链表类。
class unorder():
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head == None

    def addItem(self, item):
        temp = node(item)
        temp.setNext(self.head)
        self.head = temp
    
    def rmItem(self, item):
        current = self.head
        privious = None        ## 需要用privious来保存当前节点的上一个节点，以便于删除当前节点。
        found = False
        while current != None and not found :
            if current.getData() == item :
                found = True
            else :
                privious = current
                current = current.getNext()
        
        if current == None :   
            print('Not Found')
        else :
            if privious == None :   ## 说明item是头节点
                self.head = current.getNext()
            else:
                privious.setNext(current.getNext())

    
    def size(self):
        count = 0
        current = self.head
        while current != None :
            current = current.getNext()
            count += 1
        return count

    def search(self, item):
        found = False
        current = self.head
        while current != None :
            if current.getData() == item :
                found = True
                break
            current = current.getNext()
        
        return found

        



if __name__ == "__main__":
    l = unorder()
    l.addItem(1)
    l.addItem(2)
    l.addItem(3)
    print(l.size())
    #print(l.search(3))
    l.rmItem(1)
    l.rmItem(3)
    print(l.size())

