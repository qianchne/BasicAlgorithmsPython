### chan 2020/1/8
### problem：https://leetcode-cn.com/problems/zigzag-conversion/

### version one : 用多个堆栈来保存每行字符

def convert(myString, numRows):
    ## 注意[[] for i in range(numRows)]与[[]]*3 的区别，
    ## 参考[https://blog.csdn.net/qq_1290259791/article/details/81009164]

    newString = [[] for i in range(numRows)] 
    goDown = True
    for i in range(len(myString)):
        #index = i%numRows
        if goDown:
            index = i% (numRows*2-2)   ## 这里需要注意，是(numRows*2-2)个数为一个周期
            newString[index].append(myString[i])
            if index == numRows-1 :
                goDown = False
        else:
            index = i%(numRows-1)
            newString[index].append(myString[i])
            if index == 0:
                goDown = True
            
        

    #print(i for i in newString)        
    return newString

if __name__ == "__main__":
    print(convert('123456789', 3))