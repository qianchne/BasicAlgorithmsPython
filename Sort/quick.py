### chan 2019/12/25
### time o(nlogn), space o(logn)
### max time o(n^2)
### [Referencr](https://www.runoob.com/python3/python-quicksort.html)


### version one
### 一定要考虑的情况是，待排序列以及有序了，所以i指标一定要遍历到基准处，即i=high，否则发生交换，导致基准后的数字小于基准。

def partition(arr, low, high):
    pivot = arr[high]   ## 待排序序列的最后一个数作为基准
    j = high   

    ## i指标是从前向后遍历，j指标是从后向前遍历。
    for i in range(low, high+1):
        if arr[i] >= pivot :  
            ## 如果当前i指向的数大于基准，那么从后向前移动j指标，直到找到一个数小于基准，交换两数。
            while  (j>i) and (arr[j]>=pivot):
                j-=1
            arr[i], arr[j] = arr[j], arr[i]
        ## 当 i 遇见 j 时，说明遍历完了待排序序列。
        if i >= j :
            break
    ##此时， j = i， 且在i前的都小于基准，在j后的都大于基准，将基准移动至i处，分割序列为两个小的待排序列。
    arr[high], arr[i] = arr[i], arr[high]
    print(i)
    return i

def quicksort(arr,low, high):
    if low < high :  ## 递归结束的基本情况
        middle = partition(arr, low, high)
        quicksort(arr, low, middle-1)
        quicksort(arr, middle+1, high)

if __name__ == "__main__":
    arr = [42, 33, 25, 16, 7, 42, 25, 20, 5, 6, 4, 3, 2, 1, 19]
    high = len(arr)-1
    quicksort(arr, 0, high)
    #partition(arr, 0, 3)
    print(arr)


