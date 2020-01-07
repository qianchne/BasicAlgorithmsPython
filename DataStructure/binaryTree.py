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

## 前序遍历：先访问根节点，再访问左子树，最后访问右子树。
def preOrder(tree):
    if tree :
        print(tree.getKeyVal())
        preOrder(tree.getLeftChild())
        preOrder(tree.getRightChild())

## 后序遍历：先左子树，再右子树，最后根节点。
def postOrder(tree):
    if tree :
        postOrder(tree.getLeftChild())
        postOrder(tree.getRightChild())
        print(tree.getKeyVal())

## 中序遍历：先左子树，再根节点，最后右子树。
def midOrder(tree):
    if tree != None :
        midOrder(tree.getLeftChild())
        print(tree.getKeyVal())
        midOrder(tree.getRightChild())


#r = BinaryTree('a')
#print(r.getKeyVal())
#r.insertLeft('b')
#print(r.getLeftChild().getKeyVal())