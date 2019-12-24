### chan 2019/12/24
### 可以理解为插入排序的变形，将序列在逻辑上分组，然后进行插入排序。
### 第次分n/2组，每组2个元素，相当于n/2的2个元素数组插入排序。
### 第次分n/4组，每组4个元素，相当于n/4的4个元素数组插入排序。
### 最后一次分n/n，即对有序性较好的序列做插入排序。
### 适合中等规模和无序程度高的序列

### 希尔排序是一种动态定义间隔序列

import math

### first version
def shell1(arr):
    length = len(arr)
    ## 确定初始的gap
    gap = math.floor(length/2)
    
    ## 循环内步长递减
    while gap > 0 :
        for i in range(gap, length):
            temp = arr[i]  ## 保存代插入的值
            j = i - gap
            while j>=0 and arr[j] > temp :   ## 找到待插入数的位置，其他数依次后移一位
                arr[j+gap] = arr[j]
                j = j - gap
            arr[j+gap] = temp
        gap = math.floor(gap/2)  ## gap 减小，最终gap必会取到1，其实就是插入排序
        print(gap)

    print(arr)

if __name__ == "__main__":
    arr = [47,25,34,1,4,50,7,3,9,10,13,12,11,1,23,15,34,3,2,67,23,45,23,67,99,12,56,38,52,15,6,90]
    shell1(arr)