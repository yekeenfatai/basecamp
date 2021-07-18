from random import sample
from math import perm

def listOfThree(arr,n):
    """listOfThree: accept a list and an integer
    as input and return either  -1 (when the sum of 
    three elements in the list is)
    or a sublist of the elements of the inputted list whose
      sum is equal to the second positonal parameter"""
    try:
        
        # if (type(n) == str):
        #     return f"Check:  {n} is {type(n)} it should be an int"
        length = len(arr)
        combinations = perm(length)
        
        s = set()
        for i in range(combinations):
            samp = sample(arr,k=3)
            sampl = sum(samp)
            s.add(sampl)
            if n in s:
                return samp
        return -1
    except:
        return (f"Check!: {arr} is {type(arr)} and {n} is {type(n)} is {arr} should be a list and {n} an int")


      
   
    
