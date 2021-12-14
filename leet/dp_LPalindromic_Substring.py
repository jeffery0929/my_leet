def longestPalindrome(s) :
  if len(s) <= 1 or s == s[::-1]:
    return s
  else:
    maxlen = 1
    start = 0
    for i in range(1, len(s)):
      odd = s[i-maxlen-1 : i+1]
      print(i-maxlen-1,i+1,odd)
      even = s[i-maxlen : i+1]
      print(i-maxlen,i+1,even)
      if i-maxlen-1 >= 0 and odd == odd[::-1]:
        start = i-maxlen-1
        maxlen = maxlen + 2
        continue
      if even == even[::-1]:
        start = i-maxlen
        maxlen = maxlen + 1
  return s[start: start+maxlen]



def long(s):
    if len(s) <= 1 or s == s[::-1]:
        return s
    else:
        res=''
        reslen=0
        for i in range(len(s)):
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>reslen:
                    res=s[l:r+1]
                    reslen=r-l+1
                l-=1
                r+=1
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>reslen:
                    res=s[l:r+1]
                    reslen=r-l+1
                l-=1
                r+=1
        return(res)

print(long("bb"))


                                        
                
            

    


