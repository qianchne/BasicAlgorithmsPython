### chan 2020/1/10
### problem：https://leetcode-cn.com/problems/roman-to-integer/

### version one

def romanToInt(myString):

    ## 这种映射关系，用字典是很方便表示的
    table = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    num = 0
    for i in range(1,len(myString)):

        ## 如果前一个字符大于后一个，说明不是特殊规则，否则按特殊规则处理。
        if table[myString[i-1]] >= table[myString[i]]:
            num += table[myString[i-1]]
            #print(num)
        else :
            num -= table[myString[i-1]]
            #print(num)
    num += table[myString[len(myString)-1]]

    return num

if __name__ == "__main__":
    print(romanToInt('LVIII'))    




