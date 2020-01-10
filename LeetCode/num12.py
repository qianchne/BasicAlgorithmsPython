### chan 2020/1/10
### problem：https://leetcode-cn.com/problems/integer-to-roman/

### version one
def inToRoman(num):

    ## 罗马字母的特殊规则可以看做是新的字符，即将CD等看作是一个整体。
    roman = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]

    rString = ''
    i = 0
    while i < len(values) :
        if (num-values[i]) >= 0 :
            rString = rString + roman[i]
            num = num - values[i]
        else :
            i += 1
    return rString

if __name__ == "__main__":
    print(inToRoman(1994))
        
