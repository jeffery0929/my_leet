#dp={1:1,2:1,0:0}
def tribonacci(n):

    dp={1:1,2:1,0:0}
    def li(dp,n):
        if n in dp:
            return dp[n]
        dp[n]=li(dp,n-1)+li(dp,n-2)+li(dp,n-3)
        return dp[n]
    return li(dp,n)

l=[1,1]
l.insert(1,2)
print(l)
        
