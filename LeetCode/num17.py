### chan 2020/1/10
### problem: https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/



### 参考评论解法
def phoneNumber(letters):
    key =  {'2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']}
    ans =['']
    for num in letters :
        ### 这种写法值得学习
        ans = [ pre+suf for pre in ans for suf in key[num] ]
    
    return ans


if __name__ == "__main__":
    print(phoneNumber('234'))