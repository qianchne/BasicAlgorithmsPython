### chan 2020/1/7
### problen：https://leetcode-cn.com/problems/add-two-numbers/
### reference:https://github.com/MisterBooo/LeetCodeAnimation

### version one 
## 定义节点类
class Node():
    def __init__(self, val):
        self.item = val
        self.next = None
    
    def getItem(self):
        return self.item

    def getNext(self):
        return self.next
    
    def setNext(self, val):
        self.next = val

    def setItem(self, val):
        self.item = val
        
## 定义链表类
class myList():
    def __init__(self):
        self.head = None

    def quickBuild(self, num):
        numStr = str(num)
        for i in numStr:
            temp = Node(int(i))
            temp.setNext(self.head)
            self.head = temp
    
    def addItem(self, val):
        temp = Node(val)
        temp.setNext(self.head)
        self.head = temp 
    


def addTwoNum(num1, num2):
    str1 = myList()
    str2 = myList()
    twoSum = myList()
    carrier = 0
    str1.quickBuild(num1)
    str2.quickBuild(num2)

    while str1.head != None  and str2.head != None :
        currentVal = str1.head.getItem() + str2.head.getItem()
        if  currentVal < 10 :
            twoSum.addItem(currentVal + carrier)
            carrier = 0
        else:
            twoSum.addItem(currentVal-10 + carrier)
            carrier = 1
        str1.head = str1.head.getNext()
        str2.head = str2.head.getNext()
    

    while str1.head != None :
        currentVal = str1.head.getItem() + carrier
        if  currentVal < 10 :
            twoSum.addItem(currentVal + carrier)
            carrier = 0
        else:
            twoSum.addItem(currentVal-10 + carrier)
            carrier = 1
        str1.head = str1.head.getNext()
    
    while str2.head != None :
        currentVal = str2.head.getItem() + carrier
        if  currentVal < 10 :
            twoSum.addItem(currentVal + carrier)
            carrier = 0
        else:
            twoSum.addItem(currentVal-10 + carrier)
            carrier = 1
        str2.head = str2.head.getNext()
    
    if carrier == 1:
        twoSum.addItem(carrier)
        carrier = 0

    return twoSum
    


if __name__ == "__main__":
    twoSum = addTwoNum(9342, 10465)
    while twoSum.head != None:
        print(twoSum.head.getItem())
        twoSum.head = twoSum.head.getNext()
