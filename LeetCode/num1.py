### chan 2020/1/7
### problen：https://leetcode.com/problems/two-sum/description/
### reference:https://github.com/MisterBooo/LeetCodeAnimation

def findSum(myList, target):
    for i in range(len(myList)):
        for j in range(len(myList)):
            if myList[i]+myList[j] == target and i != j :
                break
        if myList[i]+myList[j] == target and i != j :
            break
    return i, j
        

if __name__ == "__main__":
    i, j = findSum([1,2,3,4,6,7,10], 13)
    print(i,j)


