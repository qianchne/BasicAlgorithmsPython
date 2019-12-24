### chan 2019/12/24
### ten sort algorithm

### time o(n^2), space o(1)
### first version
def Bubble1(arr):
    ## 记录每次需要遍历的数组长度，遍历完一次，长度减一，直到长度为0
    currentLen = len(arr) - 1 
    #print(currentLen)
    while (currentLen > 0):
        for i in range(currentLen):
            if (arr[i]>arr[i+1]):
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
        currentLen = currentLen - 1
    print(arr)

### second version
### add a flag to record exchange in each loop. we could stop sorting in advance if exchange doesn't happen 
def Bubble2(arr):
    currentLen = len(arr) - 1 
    while (currentLen > 0):
        for i in range(currentLen):
            exchange = 0
            if (arr[i]>arr[i+1]):
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                exchange = 1
        if exchange == 0 :
            break
        currentLen = currentLen - 1
    print(arr)
if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9,10,13,12,11]
    Bubble2(arr)



