#Q1)TRIANGLE AREA:
height=int(input("enter the length of perpendicular the triangle: "))
base=int(input("enter the length of base: "))
x=int(height*base)
area=0.5*x
print(area)

#Q2)EMAIL VERIFICATION:
for i in range(3):
    correct_email="abc@gmail.com"
    password="abc"
    e_mail=input("enter e-mail: ")
    if correct_email==e_mail:
       pas=input("enter password: ")
       if password!=pas:
           print("Incorrect password.Try again")
           pas=input("enter password: ")
       elif password==pas:
           print("logged in succesfully.")
           break
    else:
        print("incorrect e-mail.Try again.")

# #Q3)LEAP YEAR:
# input_year=int(input("enter current year: "))
# x=input_year%4
# if x==0:
#     print(f"the year {input_year} is a leap year.")
# else:
#     print(f"the year {input_year} is not a leap year.")

# #Q4)REPLACE CHAR:
# s1="lip"
# print(s1.replace("l","z"))

# #Q5)ODD ONES OUT:
# #specified way:
# s2="queen"
# s3=s2[0]+s2[2]+s2[4]
# print(s3)
# #alternate generalized way:
# str=input("Enter string:")
# str1=len(str)
# for i in range (str1):
#     if i%2==0:
#         print(str[i])

# #Q6)REMIX:
# s4="abc"
# s5="xyz"
# s6=s5[0]+s5[1]+s4[2]+" "+s4[0]+s4[1]+s5[2]
# print(s6)

#Q7)PRIME NUMBER:
no=int(input("enter your number: "))
c=0
for i in range(2,no):
    if no%i==0:
        c+=1
if c==0:
    print("is a prime number.")
else:
    no=int(input("enter your number: "))
# #Q8)PYRAMID:
# rows=int(input("enter no. of rows: "))
# for i in range(rows):
#     for j in range(i,rows):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print(2**(j),end=" ")
#     for j in range(i,0,-1):
#         print(2**(j-1),end=" ")
#     print()

# #Q9)TABLES:
# for i in range(1,9):
#     for j in range(1,11):
#         x=i*j
#         print(f"{i}*{j}={x}")

#Q10)FIBONACCI SEQUENCE:
l=[0,1]
def fibo_seq():
    x=int(l[-1])
    y=int(l[-2])
    z=x+y
    l.append(z)
    print(l)
seq=int(input("enter the number of times you'd like the sequence to be executed: "))
for i in range(seq):
  fibo_seq()

#Q12)AREA CALC:
def area_circle():
    x=3.14*(radius**2)
    print(f"area={x}")
def area_sqaure():
    x=length**2
    print(f"area={x}")
def area_triangle():
    x=0.5*(width*height)
    print(f"area={x}")
def area_rectangle():
    x=length*width
    print(f"area={x}")
for i in range(4):
    shape=input("1.Circle\n2.Sqaure\n3.Triangle\n4.Rectangle\n5.Undecided.\nenter the shape(1-5): ").lower()
    if shape=="circle":
         radius=int(input("enter radius: "))
         area_circle()
    elif shape=="rectangle" or shape=="undecided":
        length=int(input("enter length: "))
        width=int(input("enter width: "))
        area_rectangle()
    elif shape=="triangle":
        width=int(input("enter width: "))
        height=int(input("enter height: "))
        area_triangle()
    elif shape=="sqaure":
        length=int(input("enter length: "))
        area_sqaure()
    else:
        print("error.")
    


