#Name:                  Task 6.py
#Author:                Derek Baker
#Date Created:          23-02-2023
#Date Last Modified:    23-02-2023
#
#Purpose:
#
#The purpose of this program is to ask the user for number inputs. After they put in the numbers, the program will sort the numbers entered
#into lists of prime numbers and non-prime numbers


numberList = []

primeNumbers = []

nonPrimeNumbers = []

even = []

odd = []

#Defining the variables as lists for later

n = int(input("Enter how many numbers you want to add to the list: "))
#Asking the user how many number they want to add to the list

for i in range(0, n):
    number = int(input()) #will loop as many times as the user wants
  
    numberList.append(number) #adding the number that was inputted by the user into the list
      
for num in numberList:
    if num == 1:
        nonPrimeNumbers.append(num) #if the number entered is 1, it will be added to the non-prime list
        
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                nonPrimeNumbers.append(num) #checking if the number is prime and adding it to the appropriate list
                break
        else:
            primeNumbers.append(num)
            
for y in numberList:
    if (y % 2 == 0):
        even.append(y)
    else:
        odd.append(y)
        #splitting the numbers into evens and odds

print('The prime numbers are: ' + str(primeNumbers))

print('The non-prime numbers are: ' + str(nonPrimeNumbers))

print('Even numbers: ' + str(even))

print('Odd numbers: ' + str(odd))

print('The original list is: ' + str(numberList))

#printing all of the different lists including the original list 