def inst(s1,s2,s3):
    if len(s1)+len(s2)!=len(s3):
        return False
    dp={}
    def lin(i,j):
        if i==len(s1) and j==len(s2):
            return True
        if (i,j) in dp:
            return dp[(i,j)]
        if i<len(s1) and s1[i]==s3[i+j] and lin(i+1,j):
            return True
        if j<len(s2) and s2[j]==s3[i+j] and lin(i,j+1):
            return True
        dp[(i,j)]=False
        return False
    return lin(0,0)

a='aabcc'
b='dbbca'
d='aadbbcbcad'

print(inst(a,b,d))

    
        

    
