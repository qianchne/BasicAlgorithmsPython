### chan 2019/12/24
### time o(n^2), space o(1)
### 在序列较小规模和较有序的情况下效率很高

### version one 
def Insertion1(arr):

    length = len(arr)
    index = 1
    while length > index :
        for i in range(index+1):
            if arr[i]>arr[index] :
                break
        arr.insert(i, arr[index])
        arr.pop(index+1)
        index = index + 1

    print(arr)



if __name__ == "__main__":
    arr = [4,2,6,4,5,1,7,3,9,10,13,12,11]
    #arr.insert(1,1)
    #print(arr)
    Insertion1(arr)

