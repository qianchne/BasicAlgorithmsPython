### chan 2019/12/27
### 最少硬币找零钱

### version zero : 贪婪算法，先找最大币值的硬币
### 并不能解决所有的情况，例如coinValueList = [1,5,21,25]，charge = 63， 输出结果为7(25+25+5+5+1+1+1)，正确为3个21.
def findCoin0(coinValueList, charge):
    minNum = charge
    coinValueList.sort(reverse=True)  ## 降序排列币值列表
    #print(coinValueList)
    num = 0
    coinIndex = 0        ## 记录币值列表的下标，找到当前合适的最大币值。
    while charge > 0 :
        maxValue = coinValueList[coinIndex] 
        if (charge - maxValue) >= 0 :    ## 比较当前最大币值是否小于剩余待找零钱，如果是，那么找零，否则，减小当前最大币值。
            charge = charge - maxValue   
            #print(charge)
            num += 1
        else :
            coinIndex += 1
    if num <= minNum :
        minNum = num 
    return minNum


### version one :遍历所有的情况
### 可以得到所有情况下的最少找零方案，但是算法效率很低，原因是很多相同数值找零计算了很多遍。
def findCoin1(coinValueList, charge):
    minNum = charge  ## 最差情况，都是1分的硬币

    if charge in coinValueList :      ## 不加这个判断结果也是正确的，但是需要的递归次数会变多。
        return 1
    else :
        for i in [c for c in coinValueList if c <= charge] :  ## 这个写法值得借鉴 
            Num = 1 + findCoin1(coinValueList, charge-i)    ## 划分更小的问题出来
            if minNum > Num :
                minNum = Num
    return minNum


### version two : 记忆化
### 利用一个空列表保存已经计算的数值的找零方案。遍历时，判断当前找零方案是否在列表中已知了，若是，则直接停止遍历。
def findCoin2(coinValueList, charge, knowResult):
    minNum = charge
    if charge in coinValueList :
        knowResult[charge] = 1     ## 保存币值最小数量找零方案。
        return 1
    elif knowResult[charge] > 0 :  ## 判断币值是否已经在已知方案列表内，若在则直接使用此方案即可。
        return knowResult[charge]
    else:
        for i in [c for c in coinValueList if c<=charge]:
            num = 1 + findCoin2(coinValueList, charge - i, knowResult)

            if num < minNum :
                minNum = num    
                knowResult[charge] = minNum  ## 保存最少找零方案。这里可以看出，列表内保存的方案一定是最少方案。
        
    return minNum


#print(findCoin0([1,5,21,25], 63))
print(findCoin2([1,5,10,25], 63, [0]*64))
#print([c for c in [1,2,3,4] if c < 3])