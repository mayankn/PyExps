#!/usr/bin/python

'''

@author: mayanknarasimhan

Program to print the numbers from 1 to 100
if the number is divisible by 3, print Fizz
if the number is divisible by 5, print Buzz
if the number id divisible by both 3 & 5, print FizzBuzz

'''


def main():
    for i in range(1, 101):
        divisibleByThree = (i % 3 == 0)
        divisibleByFive = (i % 5 == 0)
        toPrint = ''
        if divisibleByThree:
            toPrint += 'Fizz'
        if divisibleByFive:
            toPrint += 'Buzz'
        if not toPrint:
            toPrint = i
        
        print toPrint
        
if __name__ == '__main__':
    main()