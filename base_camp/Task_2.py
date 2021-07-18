from math import sqrt

        
def is_prime(n):
    """is_prime: accept a positve integer
     and check if it is a prime to return a boolean value(True or False)"""
    try:
        #checking if n is a float to prevent a float number
        if (type(n) == float):
            return f"{n} is {type(n)}, please enter a positve integer"

        #Checking if a number is prime
        elif n < 2:
            return False
        for i in range(2,int(sqrt(n)) + 1):
            if n % i == 0:
                    return False
        return True
        
    except:
        return f"{n} is {type(n)}, please enter a positve integer"



# def main():
#     while (True):
#         try:
#             n = int(input("Please enter a positve integer: "))
#             if n < 0:
#                 continue
#             else:
#                 return is_prime(n)
#         except:    
#             continue
            


