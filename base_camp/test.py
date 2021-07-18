import unittest

from Task_1 import polaritySums
from Task_2 import is_prime
from Task_3 import array__of_prime_numbers
from Task_4 import passwordValidator
from Task_5 import spaceFiller
from Task_6 import listOfThree
from Task_7 import standardDeviation
from Task_8 import numberOfThrees
from Task_9 import palindrome
from Task_10 import frequentChr
from Bonus_Task2 import consonantMapper

class Tests(unittest.TestCase):

    

    def test1(self):
        """Checking the sum of even numbers and sum of odd numbers in a list"""
        arr = [1,2,3,4,5,6]
        err1 = 9
        err2 = 4.6
        err3 = {1:2,3:6}
        #check the sum of even numbers in the list
        self.assertEqual(polaritySums(arr)[0],12)
        #check the sum of odd numbers in the list
        self.assertEqual(polaritySums(arr)[1],9)
        #check the sum of odd in a list
        self.assertEqual(polaritySums(arr),[12,9])
        self.assertEqual(polaritySums(err1),"Note!: 9 is <class 'int'>, please enter a list of positive integer")
        self.assertEqual(polaritySums(err2),"Note!: 4.6 is <class 'float'>, please enter a list of positive integer")
        self.assertEqual(polaritySums("asdf"),"Note!: asdf is <class 'str'>, please enter a list of positive integer")
    
    def test2(self):
        """Checkin if a value is prime"""
        self.assertTrue(is_prime(47))
        self.assertFalse(is_prime(6))
        self.assertEqual(is_prime([1,2,3]),"[1, 2, 3] is <class 'list'>, please enter a positve integer")
        self.assertEqual(is_prime("asdf"),"asdf is <class 'str'>, please enter a positve integer")
        self.assertEqual(is_prime(3.5),"3.5 is <class 'float'>, please enter a positve integer")
        self.assertFalse(is_prime(True))
        self.assertFalse(False)

    def test3(self):
        """Taking out the prime numbers in a list"""
        self.assertEqual(array__of_prime_numbers([1,4,6,8,9,10]),"Array of numbers from the list entered is : [] ")
        self.assertEqual(array__of_prime_numbers([1,2,3,4,5,6,7,8,9,10]),"Array of numbers from the list entered is : [2, 3, 5, 7] ")
        self.assertEqual(array__of_prime_numbers(2),"Note!: 2  is <class 'int'>, please enter an array of positive integers.")

    def test4(self):
        """Password checking"""
        self.assertEqual(passwordValidator("abcdghgasgsa"),"0 -> 'abcdghgasgsa' is a very weak password !, it contains only letters")
        self.assertEqual(passwordValidator("1234567890"),"1 ->'1234567890' is a weak password !, it contains only numbers")
        self.assertEqual(passwordValidator("1234asdflkjhg"),"2 -> '1234asdflkjhg' is a strong password !.")
        self.assertEqual(passwordValidator("#erh$i32%34"),"3 -> '#erh$i32%34' is a very strong password")
        self.assertEqual(passwordValidator(123547768),"'123547768' is invalid")

    def test5(self):
        """Testing for word and it space filler"""
        self.assertEqual(spaceFiller("hello basecamp","##"),"hello##basecamp")
        self.assertEqual(spaceFiller("hello basecamp",2),"Note! : hello basecamp is <class 'str'> and 2  is <class 'int'>  both must be string")
        self.assertEqual(spaceFiller(2,"##"),"Note! : 2 is <class 'int'> and ##  is <class 'str'>  both must be string")
        

    def test6(self):
        """Checking the sum of sublist with 3 element if it sum upto 3"""
        self.assertIn(listOfThree([1,2,3,4,5,6],6),[[1,3,2],[1,2,3],[2,1,3],[2,3,1],[3,2,1],[3,1,2]])
        self.assertEqual(listOfThree([1,2,3,4,5,6],20),-1)
        self.assertEqual(listOfThree(2,20),"Check!: 2 is <class 'int'> and 20 is <class 'int'> is 2 should be a list and 20 an int")
        
    def test7(self):
        """Calculating the standard deviation of an array"""    
        self.assertEqual(standardDeviation([1,2,3,4]),1.2909944487358056)
        self.assertEqual(standardDeviation(16),"Note! : 16 is of type <class 'int'>, please enter a list of positve integer")
        self.assertEqual(standardDeviation([1,2,-3,7]),"-3 < 1, Please enter a positive integer")
        self.assertEqual(standardDeviation([1,2,3.8,78]),"3.8 is <class 'float'>, please change it to a positive integer")
        self.assertEqual(standardDeviation("asdf"),"Note! : asdf is of type <class 'str'>, please enter a list of positve integer")

    def test8(self):
        """Check the number of threes in a number 
        from zero to the value of the parameter"""
        self.assertEqual(numberOfThrees(35),"Output: {'count': 9, 'numbers': [3, 13, 23, 30, 31, 32, 33, 34, 35]}")
        self.assertEqual(numberOfThrees(2),"Output: {'count': 0, 'numbers': []}")
        self.assertEqual(numberOfThrees([35]),"Note! : [35] is of <class 'list'>, please enter a positve integer")
        self.assertEqual(numberOfThrees(3.0),"Note! : 3.0 is of <class 'float'>, please enter a positve integer")
        self.assertEqual(numberOfThrees("3"),"Note! : 3 is of <class 'str'>, please enter a positve integer")

    def test9(self):
        """Checking if a word is a palindrome"""
        self.assertEqual(palindrome("madam"),"Yes")
        self.assertEqual(palindrome("friend"),"No")
        self.assertEqual(palindrome(22222),"Note! : 22222 is <class 'int'>, please enter a string")
        self.assertEqual(palindrome(33.33),"Note! : 33.33 is <class 'float'>, please enter a string")

    def test10(self):
        """Checking the most frequent character(s) in a string"""
        self.assertEqual(frequentChr("afhuusnimr443o0sggg"),[{'g': 3}])
        self.assertEqual(frequentChr("adnan"),[{'a': 2}, {'n': 2}])
        self.assertEqual(frequentChr(1987999),"Note! : 1987999 is <class 'int'>, please enter a string")
        self.assertEqual(frequentChr(["a","d","n","a","n"]),"Note!: ['a', 'd', 'n', 'a', 'n'] is <class 'list'>, please input a string")

    def test11(self):
        """Mapping a consonant of the 
        English alphabet to the next one."""
        self.assertEqual(consonantMapper("hello world"),"Input: hello world\nOutput: jemmo xosmf")
        self.assertEqual(consonantMapper(12345),"Note! 12345 is <class 'int'>, please enter a string")
        self.assertEqual(consonantMapper(["hello world"]),"Note! ['hello world'] is <class 'list'>, please enter a string")
        self.assertEqual(consonantMapper("HELLO WORLD"),"HELLO WORLD is in uppercase, please put in the lower case: hello world")

if __name__ == "__main__":
    unittest.main()
