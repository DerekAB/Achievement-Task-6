#Name:                  Task 6.py
#Author:                Derek Baker
#Date Created:          23-02-2023
#Date Last Modified:    23-02-2023
#
#Purpose:
#
#The purpose of this program is to ask the user for number inputs. After they put in the numbers, the program will sort the numbers entered
#into lists of prime numbers and non-prime numbers

import math

numberList = []

primeNumbers = []

nonPrimeNumbers = []

even = []

odd = []
n = int(input("Enter how many numbers you want to add to the list: "))
  
for i in range(0, n):
    number = int(input())
  
    numberList.append(number) # adding the element
      
for num in numberList:
    if num == 1:
        nonPrimeNumbers.append(num)
        
    if num > 1:

        for i in range(2,num):
            if (num % i) == 0:
                nonPrimeNumbers.append(num)
                break
        else:
            primeNumbers.append(num)
            
print('The prime numbers are: ' + str(primeNumbers))

print('The non-prime numbers are: ' + str(nonPrimeNumbers))

print('The original list is: ' + str(numberList))