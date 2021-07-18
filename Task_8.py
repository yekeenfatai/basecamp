def numberOfThrees(n):
    """numberOfThrees : accept an integer as input 
    and returns a dictionary."""

    new = {"count":0, "numbers":[]} 
    #Checking that the input is an integer
    try:
    #Iterating through the input from 0 to the inputted value
        for i in range(n + 1):
    #Checking if an element is 3
            if ("3" in str(i)):
    #Incrementing the count of 3s
                    new["count"] += 1
    #Appending the value to the dictionary
                    new["numbers"].append(i)
    #Returning the dictionary new
        
        return f"Output: {new}"
    #Raising an warning if input is not an integer
    except:
        return f"Note! : {n} is of {type(n)}, please enter a positve integer"


