#importing is_prime from Task_2 file
from Task_2 import is_prime

# def array():
#     """array: accepts a sequence of integers 
#     and returns an array of positve integer"""
    
#     print("Enter positive integers into your array or quit by pressing n/N")
#     print("Any non positive integer will not be included")
#     arr = []
#     while True:
#         try:
#             ans = input("Do you want to enter an integer Y/N: ")
#             if ans == "n" or ans == "N":
#                 return arr
#             elif ans == "y" or ans == "Y":
#                 n = int(input("Please enter a positive integer: "))
#                 if (n > 0 and type(n) == int):
#                     arr.append(n)        
#         except:
#             print("You entered a non positive integer it will not be included in your array")
#             continue




def array__of_prime_numbers(arr):
    """Appending the element of an array to a new array when the element is a prime number and returning the new array"""
    
    new = []

    try:
        for i in arr:
            if i < 0:
                return f"Please check the array {arr} contains negative integers"
            elif is_prime(i):
                new.append(i)
        return f"Array of numbers from the list entered is : {new} "
    
    except:
        return f"Note!: {arr}  is {type(arr)}, please enter an array of positive integers."

# if __name__ == "__main__":
#     print(array__of_prime_numbers())  

# l = [-7,2.8,6,47,[1,2,3],"asdf",3.4,3.0,True]
# for i in l:
#     print(is_prime(i))


