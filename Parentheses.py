### VALID PARENTHESES SEQ ALGORITHM ###
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid
#
# An input string is valid if:
# 1. Open brackets must be closed by the same type of brackets
# 2. Open brackets must be closed in the correct order
# 3. Every close bracket has a corresponding open bracket of the same type
#
# Problem taken from LeetCode.com
# solution by NotRambi

### HOW TO USE ###
# insert a sequence of brakets
# don't write nothing for quit the execution



# validation function
def isValid(s) -> bool:
    open = []
    dct = {')':'(',']':'[','}':'{'}
    for c in s:
        if c == '(' or c == '[' or c == '{':
            open.append(c)
        n = len(open) -1
        if n == -1:
            return False
        if c in dct:
            if open[n] == dct[c]:
                open.pop()
            else:
                return False
    if(len(open) == 0):
        return True
    return False

# main
while(1):
    inputStr = input("insert a sequence of brakets: ")
    if len(inputStr) == 0:
        break
    else:
        valid = isValid(inputStr)
    if valid:
        print("is valid")
    else: 
        print("is not valid")