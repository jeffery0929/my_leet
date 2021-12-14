def twoSum(nums, target):
    dic={}
    for i,e in enumerate(nums):
        if target-e in dic:
            return [i,dic[target-e]]
        
        dic[e]=i

    return False
        


'''
def maxArea(height):
    w=len(height)-1
    cap=0
    l,r=0,len(height)-1
    while w>0 and l<r :
        temp=max(height[l],height[r])*w
        if temp>cap:
            cap=temp
        if height[l]>height[r]:
            r-=1
        
'''
def maxp(nums):
    nums=sorted(nums)
    
    return (nums[-1]*nums[-2])-(nums[0]*nums[1])

height = [1,8,6,2,5,4,8,3,7]
def maxArea(height):
    
    
    cap=0
    l,r=0,len(height)-1
    while l<r :
        temp=min(height[l],height[r])*(r-l)
        cap=max(cap,temp)
        if height[l]>height[r]:
            r-=1
        else:
            l+=1
        
    return cap

def threeSum(nums):
    if len(nums)<3:
        return []
    l=[]
    nums = sorted(nums)
    for i in range(len(nums)):
        left=i+1
        right=len(nums)-1
        

        while left<right:
            if nums[i]+nums[left]+nums[right]==0 and [nums[i],nums[left],nums[right]] not in l:
                l.append([nums[i],nums[left],nums[right]])
                left += 1
                

            elif nums[i]+nums[left]+nums[right]>0:
                right-=1
            else:
                left+=1
    
    return l

nums = [-1,0,1,2,-1,-4]
y=threeSum(nums)
print(y)
        
        







