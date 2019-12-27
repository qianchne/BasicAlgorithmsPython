### chan 2019/12/27
### 利用堆栈检查圆括号字符串是否匹配
### 利用堆栈检查符号是否匹配


import stack 
### 简单圆括号检查
def cirCheck(arr):
    s = stack.stack([])
    balance = True
    for i in range(len(arr)):
        if arr[i] == "(" :
            s.push(arr[i])
            #print(arr[i])
        else:
            if (s.isEmpty()) :
                balance = False
                #print(arr[i])
            else :
                s.pop()
    
    return balance

### 符号匹配
def symCheck(arr):
    s = stack.stack([])
    balance = True
    for i in range(len(arr)):
        if arr[i] in '({[':
            s.push(arr[i])
        else:
            if match(s.peek(), arr[i]) :
                s.pop()
            else :
                balance = False
                break
    return balance

def match(a,b):
    opens = '({['
    ends = ')}]'
    return opens.index(a) == ends.index(b)


if __name__ == "__main__":
    arr = ['(','[',']','{','}',')']
    #print(cirCheck(arr))
    print(symCheck(arr))

            

