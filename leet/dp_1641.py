vowels=['a','e','i','o','u']
def countVowelStrings(n):
    if n==1:
        return 5
    l=[1]*5
    dp={1:l}
    
    def plu(a):
        big=sum(a)
        result=[big]
        for n in a:
            big=big-n
            result.append(big)
        result.pop()
        return result
    def lic(dp,n):
        if n in dp:
            return dp[n]
        dp[n]=plu(lic(dp,n-1))
        return dp[n]
    return sum(lic(dp,n))

print(countVowelStrings(33))


    