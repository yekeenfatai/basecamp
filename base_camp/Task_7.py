#importing a stdev
from statistics import stdev

def standardDeviation(arr):
    """standardDeviation: accepts an array of positve integers and
    returns a float"""

    #Ensuring that the input elements' is an integer 
    try:
        for i in arr:
    #verifying that each element is a positve integer
            if (i < 1):
                return  f"{i} < 1, Please enter a positive integer" 
            elif(type(i) != int):
                return f"{i} is {type(i)}, please change it to a positive integer"
    #returning the standard deviation of the input
        return stdev(arr)
    #Raise a warning when input is not an array of integers
    except:
        return f"Note! : {arr} is of type {type(arr)}, please enter a list of positve integer"

