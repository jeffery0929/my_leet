def generate(numRows):

    dp={1:[1],2:[1,1]}
    if numRows==1:
        return [dp[1]]
    if numRows==2:
        return [dp[1],dp[2]]
    
    def lisadd(a):
    
        result=[]
        b=a+[0]
        a=[0]+a

        for i in range(len(a)):
            result.append(b[i]+a[i])

        return result
    def lic(dp,numRows):
        if numRows in dp:
            return dp[numRows]
        dp[numRows]=lisadd(lic(dp,numRows-1))
        return dp[numRows]
    
    lic(dp,numRows)
    l=[]
    for i in range(1,numRows+1):
        l.append(dp[i])
    return l

        
print(generate(1))

        
    
    
