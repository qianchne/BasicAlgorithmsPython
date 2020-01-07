### chan 2020/1/7
### phaseTree 

import binaryTree 
import stack

def buildPhaseTree(equation):
    pStack = stack.stack()
    eTree = binaryTree.BinaryTree('')
    currentTree = eTree

    for i in equation :
        if i == '(' :
            #print(i)
            pStack.push(currentTree)
            currentTree.insertLeft('')
            currentTree = currentTree.getLeftChild()
            #print(pStack.size())     

        elif i not in ['+', '-', '*', '/', ')']:
            #print(i)
            currentTree.setRootVal(int(i))
            currentTree = pStack.peek()
            pStack.pop()
            #print(pStack.size())     
            
        elif i in ['+', '-', '*', '/']:
            #print(i)
            currentTree.setRootVal(i)
            pStack.push(currentTree)
            currentTree.insertRight('')
            currentTree = currentTree.getRightChild()
            #print(pStack.size())     
            
        elif i == ')' :
            #print(i)
            currentTree = pStack.peek()
            pStack.pop()
            #print(pStack.size())     

    return eTree

e = buildPhaseTree('((1+5)*3)')
#print(e.getKeyVal())
binaryTree.midOrder(e)


