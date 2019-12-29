### chan 2019/12/29

class BinaryTree():
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None :
            self.leftChild = BinaryTree(newNode)
        else:
            tempNode = BinaryTree(newNode)
            tempNode.leftChild = self.leftChild
            self.leftChild = tempNode
    
    def insertRight(self, newNode):
        if self.rightChild == None :
            self.rightChild = BinaryTree(newNode)
        else:
            tempNode = BinaryTree(newNode)
            tempNode.rightChild = self.rightChild
            self.rightChild = tempNode
    
    def getLeftChild(self):
        return self.leftChild
    
    def getRightChild(self):
        return self.rightChild
    
    def setRootVal(self, obj):
        self.key = obj
    
    def getKeyVal(self):
        return self.key
    
r = BinaryTree('a')
print(r.getKeyVal())
r.insertLeft('b')
print(r.getLeftChild().getKeyVal())