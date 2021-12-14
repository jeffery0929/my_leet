def getConcatenation(nums):
    l=nums*2
    return l


def addrung(rungs,dist):
    rungs.insert(0,0)
    lab=0
    for i in range(len(rungs)-1):
        if rungs[i]+dist<rungs[i+1]:
            c=rungs[i+1]-rungs[i]-1
            lab=lab+c//dist
    return lab
        
    
            

rungs = [3,6,8,10]
dist = 3
print(addrung(rungs,dist))
        