#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 15:43:27 2021

@author: yelicheng
"""
memo={}
def fib_m(n,memo):
    #print(memo)
    if(n in memo):
        return memo[n]
    if(n<=2):
        return 1
    memo[n]=fib_m(n-1,memo)+fib_m(n-2,memo)
    return memo[n]

print(fib_m(50,memo))

def fib_t(n):
    table=[0]*(n+1)
    table[1]=1
    for i in range(2,len(table)):
        
        table[i]=table[i-1]+table[i-2]
        
        
        
    return table[n]

    
print(fib_t(50))

def countB(n):
    table=[0]
    if(n==0):
        return table
    
    for i in range(n):
        table.append(sum(list(map(int,bin(i+1)[2:]))))
        
    return table

print(countB(2))

nums = [-2,1,-3,4,-1,2,1,-5,4]

def max_sub(nums):
    if len(nums) == 0: return 0
    maxValue = nums[0]
    sum = nums[0]
    for index in range(1, len(nums)):
        if nums[index] > sum and sum < 0:
            sum = nums[index]
        else:
            sum += nums[index]
        maxValue = max(maxValue, sum)
    return maxValue

print(max_sub(nums))


