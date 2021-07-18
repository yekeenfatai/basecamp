def consonantMapper(word):
    """consonantReplacement: It accepts lowercase strings and output a string.
    Each consonant at a position is map to the next consonant"""

    #check if parameter is not a string
    try:
        #checks if the parameter is uppercase  
        if word.isupper():
            return f"{word} is in uppercase, please put in the lower case: {word.lower()}"

        #do this if parameter is lowercase
        word = word.lower()
        consonantmaps = {"z": "b","d":"f","h":"j","n":"p","t":"v"}
        consonantAsci = [98,99,100,102,103,104,106,107,108,109,110,112,113,114,115,116,118,119,120,121,122]
        vowels = ["a","e","i","o","u"]
        newword = ""

        #looping through the parameter
        for i in word:
            #converts each letter of the parameter to its ascci code
            alphabet_asci = ord(i)

            #map and concatenate each letter from the parameter to the newword
            if i in consonantmaps:
                newword += consonantmaps[i]
            elif alphabet_asci in consonantAsci:
                j = alphabet_asci + 1
                j = chr(j)
                newword += j
            else:
                newword += i
        #return a string
        return f"Input: {word}\nOutput: {newword}"
    except:
        #return this if the parameter is a string
        return f"Note! {word} is {type(word)}, please enter a string"
    




         