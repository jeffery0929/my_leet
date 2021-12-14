s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
def restoreString(s,indices):
    result=""
    for i in range(len(indices)):
        result+=s[indices.index(i)]
    return result

print(restoreString(s,indices))
