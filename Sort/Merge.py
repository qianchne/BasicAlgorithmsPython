### chan 2019/12/24
### time o(nlogn), space o(n)
### 没有指针，导致怎么判断是否遍历完了，很麻烦。
### 没写完，很麻烦。

import math

### version one 
def Merge(arr):
    length = len(arr)
    print(length)
    gap = 2
    newarr = []
    while gap < math.ceil(length/2):
        for i in range(0, length, gap):
            index1 = i
            index2 = i + int(gap/2)
            while ((index1 - i) < gap/2) and ((index2 - (i+int(gap/2))) < gap/2) : 
                print(index1)
                print(index2)
                if arr[index1] < arr[index2] :
                    newarr.append(arr[index1])
                    index1+=1
                else :
                    newarr.append(arr[index2])
                    index2+=1 

            if index1 - i == gap/2:
                while ((index2 - (i+int(gap/2))) < gap/2) :
                    newarr.append(arr[index2])
                    index2+=1
            else:
                while ((index1 - i) < gap/2) :
                    newarr.append(arr[index1])
                    index1+=1
        arr = newarr
        newarr = []
        gap = gap * 2


        



    print(arr)
 



if __name__ == "__main__":
    arr = [47,25,34,1,4,50,7,3,9,10]
    #arr.insert(1,1)
    #print(arr)
    Merge(arr)

