### chan 2020/1/8
### problen：https://leetcode-cn.com/problems/median-of-two-sorted-arrays/
### reference:https://github.com/MisterBooo/LeetCodeAnimation

def midNum(l1, l2):
    tStack = []
    index1 = 0
    index2 = 0
    empty1 = False
    empty2 = False

    ## 将l1和l2中最小的数，依次入堆栈。直到一半的数入堆栈。
    for i in range(int((len(l1)+len(l2))/2) + 1):
        if l1[index1] < l2[index2] :
            tStack.append(l1[index1])
            index1 += 1
            if index1 == len(l1):  ## 判断是否l1已经空了
                empty1 = True
                break
        else:
            tStack.append(l2[index2])
            index2 += 1
            if index2 == len(l2):  ## 判断是否l2已经空了
                empty2 = True
                break

    while i < int((len(l1)+len(l2))/2):
        if empty1 :
            tStack.append(l2[index2])
            index2 += 1
        elif empty2:
            tStack.append(l1[index1])
            index1 += 1
        i += 1

    if len(tStack)%2 == 0 :
        return (tStack.pop()+tStack.pop())/2
    else :
        return tStack.pop()
        

if __name__ == "__main__":
    print(midNum([1], [2]))
