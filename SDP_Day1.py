# Day1 of SDP python 
#=============================================Exercise 1===========================================#
#WAP for ADD, MUL, DIV, SUB
a = 10
b = 20
print(a+b)   #Addition
x = 40
y = 20
print(x*y)   #Multiplication
a = 100
b = 50
print(a/b)   #Division
x = 90
y = 40
print(x-y)   #Subtration

#WAP to calculate simple interest 
p = 50000
r = 8
t = 1
si = (p * r * t)/100
print('The simple interest is', si)

#WAP for swaping using third variable
num1 = 29
num2 = 56
num3 = num1
num1 = num2
num2 = num3
print(num1)
print(num2)

#WAP for swapping without using third variable
a = 80
b = 50
a , b = b, a
print('Value of a is', a)
print('Value of b is', b)

#WAP to calculate gross sal from basic sal(HRA=30%, TA=40%, DA=20%)
basic_sal = int(input('Enter your basic salary:'))
HRA =float(basic_sal* 0.3)
TA = float(basic_sal*0.4)
DA = float(basic_sal*0.2)
PF = float((basic_sal+DA)*0.11)    #PF = 11%
netpay = float(basic_sal+HRA+TA+DA+PF)
gross_sal = float(netpay - PF)
print('Gross salary is', gross_sal)

#WAP to find circumference of circle
r = 5
C = 2*3.14*r
print('Circumference of a circle is',C)

#WAP to find area of circle
r = 5
area = 3.14*r*r
print('Area of a circle', area)

#WAP to enter height of user in feets and convert it into inches and centimeter 1feet = 12inch  1inch=2.54 cm4
ht_ft = float(input('Enter your height in feets'))
ht_inch = ht_ft* 12
print('Height in inches',ht_inch)
ht_cm = ht_inch * 2.54
print('Height in cm',ht_cm)

#WAP to take centigrate temperature and convert it into ferhanite temperature f = 1.8*c+32
Temp_C = int(input('Enter temperature in Celcius'))
Temp_F = 1.8*Temp_C+32
print('Temperature in ferhanite', Temp_F)


 



