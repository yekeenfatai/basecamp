def spaceFiller(word,filler):
    """space_filler: accepts two strings as input and returns
    a string"""

    #Verifying that inputs are strings
    try:
         return word.replace(" ",filler)
    #Raising a warning when either or both inputs is or are string(s)
    except:
        return f"Note! : {word} is {type(word)} and {filler}  is {type(filler)}  both must be string"


# a = "hello basecamp"
# b ="##"
# c = 2

# print(spaceFiller())