# Day2 of SDP python 
#===========================================Exercise 2=============================================#

#WAP to calculate sum of natural number from 1 to 10
sum = 0
i = 1 
while i<=10:
    sum = sum + i
    i = i+ 1
print(sum)

#WAP to calculate factorial of any number 
i = 1
fact = 1
n = int(input('Enter a number'))
if n<0:
    print("Factorial doesn't exist for negative number")
elif n==0 or n==1:
    print("Factorial of", n ,'is 1')
else:
    for i in range(1,n+1): #i = 5
        fact = fact*i  #fact=120
    print('Factorial of', n, 'is', fact)

#WAP to calculate fibonacci series 0 1 1 2 3 5 8 13
n = int(input('Enter a number'))
f0 = 0
f1 = 1
i = 0
fn = 0
if n<0:
    print('Negative numbers are not allowed')
elif n==0:
    print('Fibonacci series of 0 is 0')
else:
    for i in range(1, n): 
        fn = f0 + f1
        f0 = f1
        f1 = fn
        print(f1)
    print('Fibonacci series of', n, 'is',f1 )

#WAP to calculate LCM, HCF, GCD
n1 = float(input('Enter first number'))
n2 = float(input('Enter second number'))
gcd = 0
if (n2 == 0):
    print(n1)
print(gcd(n2,n1%n2))
 
#WAP to check leap year
year = int(input('Enter year'))
if year%400 == 0:
    print('It is a leap year')
elif year%4 ==0:
    print('It is a leap year')
elif year%100 == 0:
    print('Is a not a leap year')
else:
    print('Not a leap year')

#WAP to check armstong number
num = int(input("Enter a number: "))
sum = 0
temp_num = num
while temp_num > 0:         #temp = 1
   digit = temp_num % 10    #digit = 1
   sum += digit ** 3        #sum= 152+1*1*1 = 153
   temp_num //= 10          #temp = 0
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

#WAP to find palindrome number
n=int(input("Enter number:"))     #2002
temp_num = n
rev=0
while(temp_num >0):       #temp_num = 0
    dig=temp_num %10      #dig = 2
    rev=rev*10+dig        #rev = 200*10+2= 2002
    temp_num //=10        # temp_num  = 0
if(n==rev):
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")

#WAP Enter five integer number and find max number (using simple if)
num = int(input("Enter a Number :"))
Largest=0
while (num > 0):             #num=0
    remainder=num%10         #remainder = 1
    if Largest<remainder:    #5<5
        Largest = remainder  # largest = 5
    num //= 10               # num = 0
print("The Largest Digit is :", Largest)
 
#WAP Enter five integer number and find smallest number (using simple if)
num = int(input("Enter a Number :"))   #12345
smallest= num
while (num > 0):                #num=0
    remainder=num%10            #remainder = 1
    if smallest>remainder:      # 12345 > 1
        smallest = remainder    # smallest = 1
    num //= 10                  # num = 0
print("The Smallest Digit is :", smallest)

#WAP to display exact pattern as below using zip() 
'''
1   5
2   4
3   3
4   2
5   1
'''
num = [ "1", "2", "3", "4", "5" ]
reverse_num = ["5","4","3","2","1"]
for n, r_n in zip(num,reverse_num):
    print ( "%s   %s" %(n, r_n))

#WAP  to convert a alphabet into its ASCII equivalent
char = (input("Enter a character: "))
print("The ASCII value of",char ,"is", ord(char))












