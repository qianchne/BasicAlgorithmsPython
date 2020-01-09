### chan 2020/1/9
### problem：https://leetcode-cn.com/problems/container-with-most-water/

def containerWater(container):
    volum = 0
    preP = 0    ## 类似于指向列表首的指针
    backP = len(container)-1  ## 类似于指向列表尾的指针

    while preP < backP :
        ## 计算储水量
        tempVolum = (backP - preP)* min(container[preP], container[backP])
        if tempVolum > volum :
            volum = tempVolum

        ## 将短的隔板向中心移动    
        if container[preP] < container[backP] :
            preP += 1
        else :
            backP -= 1

    return volum

if __name__ == "__main__":
    print(containerWater([1,8,6,2,5,4,8,3,7]))
