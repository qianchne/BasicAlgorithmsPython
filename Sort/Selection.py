### chan 2019/12/24
### time o(n^2), space o(1)

### first version
def Selection1(arr):
    length = len(arr)
    while (length > 0):
        index = 0
        for i in range(length):
            if arr[i] > arr[index]:
                index = i
            temp = arr[length-1]
            arr[length-1] = arr[index]
            arr[index] = temp
        length = length - 1
    print(arr)
    

if __name__ == "__main__":
    arr = [4,2,6,4,5,1,7,3,9,10,13,12,11]
    Selection1(arr)