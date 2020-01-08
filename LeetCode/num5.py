### chan 2020/1/8
### problem：https://leetcode-cn.com/problems/longest-palindromic-substring/
### reference:https://github.com/MisterBooo/LeetCodeAnimation

### version one : 中心扩展法。关键在于解决奇偶个数的回文序列
def palindromicSubstring(myString):

    ## 记录回文个数
    maxNum = 1 
    for i in range(len(myString)*2-1) : ## 中心点有2*n-1个
        ## 如果i为2倍数，中心点为string中的数字，index设为1，否则设为0.5.
        if i%2 == 0 :
            index = 0
        else:
            index = 0.5
        
        ## 中心扩展并比较
        while myString[int(i/2-index)] == myString[int(i/2+index)]:
            if maxNum < index*2 + 1 :
                maxNum = index*2 + 1
            index += 1

            ## 控制向两边扩展的范围不超出索引范围
            if i/2-index < 0 or i/2+index > len(myString)-1 :
                break
    return int(maxNum)

if __name__ == "__main__":
    print(palindromicSubstring('12332611')) 



        
