def palindrome(word):
    """Palindrome accept a string as input and output 
    either Yes or No base on the value of the input"""

    #verifying the the type of input
    try:
        k = 0
    #convert the input value to lowercase
        word = word.lower()
    #Looping through the input value
        for l in word:
            k -= 1
    #checking each element of the string 
            if l != word[k]:
    #output No if input string is not a palindrome
                return "No"               
    #output Yes if input string is a palindrome
               
        return "Yes"
    #Raising an warning when the input is not  type string
    except:
        return f"Note! : {word} is {type(word)}, please enter a string"
 
