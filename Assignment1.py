# the next line is to ask user the input to enter any two number and save it to x and y
#question no 1
y=input('enter one number')
x=input('enter one number')

print('this is the sum',int(x)+int(y))
print('this is the dif',int(x)-int(y))




#this is question no 3
l=input('enter the length of the rectangle')
b=input('enter the breath of the rectangle')
print('the area of rectangle is ',int(l)*int(b))
print('the Perimeter of rectangle is', int(2)*int(l)+int(b))
# int(a)
# print(a)



#Question no 4
age =23
name=input('what is your name')
s='My name is : '+name+' and age is : '+str(age)
print(s)
x=float(input('enter the first number x:'))
y=float(input('enter the first number y:'))

z= x**3+3*x**2*y+3*x*y**2+y**3
print(z)

2
i=True
while(i):
    choice_num=int(input("Enter the number 0 or 1. \n 0 to Enter the program and 1 to exit the program \n NOTE:PLEASE ENTER 0 TO EXIT  "))
    if choice_num==1:
        first = float(input("Enter the first number"))
        second =float(input("Enter the Second number"))
        third =float(input("Enter the Third number"))
        if first>second and first != second and third:
            print("First greater" +str(first))
        elif second>first and third<second:
            print("The second number is greater" +str(second))
        elif third>first and second<third :
            print("The Third number is greater" +str(third))
            break
        else:
            print("There ia a problem because you have entered the same number for first,second and third number please input the valid numeric data")
    elif choice_num == 0:
        print("Existing the program")
        break
    else:
        print("PLEASE ENTER 0 OR 1 ONLY \n ..QUITING THE PROGRAM...................")
        break

#3 GCD using while loop 

print("This  is the program that calculates the GDC(greatest common divisor) of two number using EUclidean algorithm)")
a=int(input("enter the first number :"))
b=int(input("enter the second number :"))
x = 1
while (x <= a):
    if (a % x == 0) and (b % x == 0):
        gcd = x
    x += 1
    break
print("the GCB is : " +str(gcd))
print(type(x))

#oppp

#fibonacci
n1,n2=0,1
i= int(input("Enter the no of series :"))
if(i<=0):
    print(".....")

elif(i==1):
    print("0")
else:
    print("0")
    print("1")
    for x in range(i): #RANGE(I) - [0,I)
        if(x<=1):
            continue #bypass the code below continue and enter the loop again
        nf=n1+n2
        n1,n2=n2,nf
        print(nf) 
    

#stars 
n=int(input("enter the no of stars :"))
for i in range(n):  #[0,n)
    print("*" * (i+1))

#
n=(int(input("enter the number")))
for i in range(n):
    print(i+3)
    
this is question on 2 
defining the function to calculate the grade based on the average 
def determine_grade(average):
    if 70<= average <= 100:
        return 'A'
    elif 60<= average <70:
        return 'B'
    elif 50 <= average <60:
        return 'C'
    elif 43 <= average < 49:
        return 'D'
    elif 40 <= average <42:
        return 'E'
    else:
        return 'F'
    # Use an infinite while loop with break to exit on user request
while True:
    # Ask the user to enter the name of a student or -1 to exit
    name = input("Enter the name of a student or -1 to exit: ")
    # If the user enters -1, break the loop
    if name == '-1':
        break
    # Ask the user to enter the marks obtained in 3 subjects
    subject_1 = float(input("Enter the marks obtained in subject 1: "))
    subject_2 = float(input("Enter the marks obtained in subject 2: "))
    subject_3 = float(input("Enter the marks obtained in subject 3: "))
    # Calculate the total and average marks
    total = subject_1 + subject_2 + subject_3
    average = total / 3.0
    # Call the function to determine the grade based on the average
    grade = determine_grade(average)
    # Print the output
    print(f"The name of the student is {name}")
    print(f"The marks obtained in subject 1 is {subject_1}")
    print(f"The marks obtained in subject 2 is {subject_2}")
    print(f"The marks obtained in subject 3 is {subject_3}")
    print(f"The average marks is {average:.2f}")
    print(f"The overall grade is {grade}")

    # ask the user how many  inputs are required 
num=int(input("enter a number in the list :"))

list1 =[]
for i in range ( num ):
    num1=float(input("enter the number :"))
    list1.append(num1)
print(list1)
sum_odd, sum_even = 0,0
for element in list1:
    if num %2==0:
        sum_even += num
    else:
        sum_odd += num
print("the list ",sum_even, sum_odd)
print(num)

max_value, min_value= list1[0], list1[0] 6
slicing 
slic=[1,2,3,4,5,6,7,8,9,9]
print(slic[2:])
x='this is class'
print(x[0])
print(x[-1:-3:-1])#this goes right to left becouse the step is -1 
print(x[::1]) 
print(x[::-1])
print(x[-1:5:-1])

## is this name Palidrome

a=input('enter the string to check from plaindrom')
print
x=(a[::1])
y=(a[::-1])
if x==y:
    print('thid is palidrome')
else:
    print('NO')
    print ('not palidrome ')

#input and print the sum 
n=int(input('enter a number'))
sum =n+1
print(sum)
# for i in range(1,n+1)

    