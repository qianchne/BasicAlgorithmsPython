### chan 2020/1/10
### problem：https://leetcode-cn.com/problems/longest-common-prefix/

### version one : 暴力两两比较
def longestCommonPrefix(strs):
    commonPrefix = ''
    tempcommonPrefix = strs[0]
    i = 0
    index = 0
    while i < len(strs):
        while index < min(len(tempcommonPrefix), len(strs[i])) and tempcommonPrefix[index] == strs[i][index] :
            commonPrefix = commonPrefix + tempcommonPrefix[index]
            index = index + 1
        tempcommonPrefix = commonPrefix
        if i != len(strs)-1 :
            commonPrefix = ''
        i = i + 1
        index = 0
    
    return commonPrefix

if __name__ == "__main__":
    print(longestCommonPrefix(['applew', 'applewatch', 'apple', 'applew']))