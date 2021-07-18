def frequentChr(word):
    """frequentChr: accept a string as input and returns
    the most frquently occured element as dictionary"""

    #Verifying that the input is type string 
    try:
    #To ensure that the parameter is a string not an array
        if (type(word) in [list,set,dict]):
            return f"Note!: {word} is {type(word)}, please input a string"
        new = {}
    #iterating through the input
        for i in word:
    #Updating the dictionary (new).
            if (i in new):
                new[i] += 1
            else:
                new[i] = 1
    #Geting the element(s) with the highest frquency
        maxValue = max(new.values())
        arr = []
        for i,j in new.items():
            if j == maxValue:
                arr.append({i:j})
    #returning a list of elements(s) 
        return arr
    #Raising a warning when input is not string
    except:
        return f"Note! : {word} is {type(word)}, please enter a string"

