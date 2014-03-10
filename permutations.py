#!/usr/bin/python -tt

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys

permutationStrings = set()
out = []
    
# Define a main() function that prints a little greeting.
def main():
    string = 'abhi'
    # string = 'abc'
    strings = permutations(string)
    print sorted(strings, key=len)
    
def permutations(string):
    if len(string) == 1:
        permutationStrings.add(string)
        return permutationStrings
    lchar = string[0]
    remainingString = string[1:]
    for str in permutations(remainingString):
        out.extend(insertAtAllPositions(lchar, str))
    permutationStrings.update(set(out))
    return permutationStrings
    
def insertAtAllPositions(lchar, str):
    newStr = str[:] + ' '
    length = len(newStr)
    output = []
    # print length
    for i in range(0, length):
        char = newStr[i]
        tempStr = newStr[0:i] + lchar + newStr[i:]
        output.append(tempStr.strip())
    return output

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
