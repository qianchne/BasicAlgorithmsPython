### chan 2020/1/10
### problem：https://leetcode-cn.com/problems/3sum/

from num1 import findSum as twoSum

'''
### version one: 考虑利用num1 中的两数之和来做这一题，实际上不可行，难以去除重复的情况。
def threeSum(myList):
    ## 去除重复的数字
    myList.sort()
    tempList = myList
    result = []
    threeGroup = []
    for i in range(len(myList)):
        c = myList[i]
        a, b = twoSum(tempList, -c)
        
        threeGroup.append(c)
        threeGroup.append(tempList[a])
        threeGroup.append(tempList[b])

        result.append(threeGroup)
        threeGroup = []
        tempList = myList
    
    return result
'''
### version : 双指针
def threeSum2(myList):

    ## 先排序
    myList.sort()
    result = []
    for i in range(len(myList)):

        ## 如果两数字重复，则跳过此次匹配
        if i > 0 and myList[i] == myList[i-1] :
            continue
        ## 如果三元组中最小的数大于0，则结束了。这里可见先排序的好处
        if myList[i] > 0 :
            break

        l = i + 1  # left pointer
        r = len(myList)-1 # right pointer
        
        while l < r :
            s = myList[i] + myList[l] + myList[r]

            if s == 0 :
                result.append([myList[i], myList[l], myList[r]])
                ## 避免重复项
                while l<r and myList[l] == myList[l+1]:
                    l += 1
                while l<r and myList[r] == myList[r-1]:
                    r -= 1
                l += 1
                r -= 1

            elif s < 0 : 
                l += 1
            
            else :
                r -= 1
    
    return result

if __name__ == "__main__":
    print(threeSum2([-2,-4,-5,-1,0,1,2,3,6,7]))






