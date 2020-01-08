### chan 2020/1/8
### problen：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
### reference:https://github.com/MisterBooo/LeetCodeAnimation

### version one 
def findMaxChild(myList):
    if myList != '' :
        maxNum = 1
    num = 0
    childlist = []
    for i in myList:
        childlist.append(i)
        if i in childlist :
            if num > maxNum:
                maxNum = num
                num = 0
                childlist = []
        num = num + 1
    return maxNum
        

if __name__ == "__main__":
    print(findMaxChild('pwwkew'))