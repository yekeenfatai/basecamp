def polaritySums(arr):
    """arraySums: accepts an array of positve integers as input and returns an array of the sums
    of even and odd number as output"""

    #Verifying that the input is an array of positve integer positve
    try:
        even = 0
        odd = 0
        new = []
        for i in arr:
            if (i < 0 or type(i) == float):
                return f"Note!: {i} is {type(i)} not a positve integer"
            else:
                if (i % 2 == 0):
                    even += i
                else:
                        odd += i
        new.append(even)
        new.append(odd)
    #returning an array
        return new
    #
    except:
        return f"Note!: {arr} is {type(arr)}, please enter a list of positive integer"

