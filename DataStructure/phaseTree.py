### chan 2020/1/7
### phaseTree 

import binaryTree 
import stack

def buildPhaseTree(equation):
    pStack = stack.stack()

    ## etree 保存根节点
    eTree = binaryTree.BinaryTree('')
    currentTree = eTree

    for i in equation :

        ##  如果是（，用堆栈保存父节点，currentTree移动到左节点
        if i == '(' :
            #print(i)
            pStack.push(currentTree)
            currentTree.insertLeft('')
            currentTree = currentTree.getLeftChild()
            #print(pStack.size())     

        ##  如果是数字，对当前节点赋值。一定要记住，赋完值后，要出堆栈，回到父节点。到这里就完成了一个小算式。
        elif i not in ['+', '-', '*', '/', ')']:
            #print(i)
            currentTree.setRootVal(int(i))
            currentTree = pStack.peek()
            pStack.pop()
            #print(pStack.size())     

        ## 如果是运算符，对父节点赋值。用堆栈保存父节点，currentTree移动到右节点。    
        elif i in ['+', '-', '*', '/']:
            #print(i)
            currentTree.setRootVal(i)
            pStack.push(currentTree)
            currentTree.insertRight('')
            currentTree = currentTree.getRightChild()
            #print(pStack.size())     
        ## 如果是），出堆栈，回到父节点。    
        elif i == ')' :
            #print(i)
            currentTree = pStack.peek()
            pStack.pop()
            #print(pStack.size())     

    return eTree

e = buildPhaseTree('((1+5)*3)')
#print(e.getKeyVal())
binaryTree.midOrder(e)


