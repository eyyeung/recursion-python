def recursionSum(nums):
    # base case
    if len(nums) == 1:
        return nums[0]
    # the recursion steps, keep calling one smaller and building up the stack
    else:
        return nums[0] + recursionSum(nums[1:])

# testing recursionSum
# print(recursionSum([1,3,5,7,9])) # should get 25

def recursionToBase(integer,base):
    if integer<0 or isinstance(integer,int)==False:
        raise ValueError("Positive Integer only")
    elif base>16 or base<=0 or isinstance(integer,int)==False:
        raise ValueError("Base from 1 to 16 only")
    convert = "0123456789ABCDEF"

    #base case
    if integer < base:
        return convert[integer]
    
    else:
    # recursion call to itself with integer divide by base and adding the converted remainder in the end
        return recursionToBase(integer//base,base) + convert[integer%base]

#testing recursionToBase
# print(recursionToBase(188,16)) # should get BC
# print(recursionToBase(18,16.2)) # should raise ValueErorr, base 1 to 16, integers only
# print(recursionToBase(1.2,16)) # should raise ValueError, value should be positive integer only

def recursionReverse(for_str):
    if len(for_str) == 1:
        return for_str
    else:
        return for_str[-1] + recursionReverse(for_str[:-1])

#testing recursionReverse
# print(recursionReverse("abcde")) #should get edcba
# print(recursionReverse("Hello World"))  # should get dlroW olleH

# need to remove white space and punctuation first
def removePunct(phase):
    clean_phase = ""
    for word in phase:
        if word.isalpha() == True:
            clean_phase +=word.lower()
    return clean_phase

def recursionPalindrome(clean_phase):
    # base case
    if len(clean_phase) <= 1:
        return True
    elif clean_phase[0] != clean_phase[-1]:
        return False
    elif clean_phase[0] == clean_phase[-1]:
        recursionPalindrome(clean_phase[1:-1])
        return True

# overall function to test if a phase or word is a palindrome
def testPalindrome(phase):
    clean_phase = removePunct(phase)
    return recursionPalindrome(clean_phase)

# clean_phase = removePunct("Reviled did I live, said I, as evil I did deliver.")
# print(clean_phase) # should get : revileddidilivesaidiasevilididdeliver
# print(testPalindrome("kay")) # should get False
# print(testPalindrome("Live not on evil")) # should get True
# print(testPalindrome("Go hang a salami; I’m a lasagna hog.")) # should get True
# print(testPalindrome("Reviled did I live, said I, as evil I did deliver")) # should get True


# accepts positive exponent only, return base to the power of exp
def power(base, exp):
    if exp == 0:
        return 1
    elif exp<0 or isinstance(exp,int)==False:
        raise ValueError('exponent can only be a positive integer')
    return base*(power(base,exp-1))

# testing our own power function
# print(power(4,3)) # should be 64
# print(power(2,0)) # should be 1
# print(power(-2,2))  # should be 4

# lucase number generate the next number of the sequence by adding up the previous two numbers
# 2,1,3,4,7,11, ...
# n is straightly postiive integer
def lucas_number(n):
    if n==0:
        return 2
    elif n==1:
        return 1
    return lucas_number(n-1) + lucas_number(n-2)

#print(lucas_number(9)) #should be 76