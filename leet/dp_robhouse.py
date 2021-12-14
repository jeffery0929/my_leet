def rob(l):
    rob1,rob2=0,0
    for n in l:
        temp=max(rob1+n,rob2)
        rob1=rob2
        rob2=temp

    return max(rob1,rob2)
    
print(rob([1,2,3,1]))