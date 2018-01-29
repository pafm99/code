# function which return reverse of a string
def reverse(inputString):
    return inputString[::-1]
    
# function which checks string and reverse of the string 
def checkPalindrome(inputString):
    # Calling reverse function
    rev = reverse(inputString)
    if (inputString == rev):
        return True
    return False
