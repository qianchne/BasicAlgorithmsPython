### chan 2020/1/10
### problem: https://leetcode-cn.com/problems/valid-parentheses/

### version one : 利用堆栈
def isValid(s):
    stack = []
    left = '([{'
    right = ')]}'
    for character in s :
        if character in left :
            stack.append(character)
        
        if character in right :
            if stack != [] and right.index(character) == left.index(stack.pop()) :
                #print(stack)
                continue
            else :
                return False
    if stack == []:
        return True
    else :
        return False

### version two : 利用python提供的函数
def isValid2(s):
    while '{}' in s or '[]' in s or '()' in s :
        s = s.replace('{}', '')
        s = s.replace('[]', '')
        s = s.replace('()', '')
    if s == '':
        return True
    else :
        return False
if __name__ == "__main__":

    print(isValid('([)]'))
    print(isValid2('([)]'))

