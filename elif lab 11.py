#integer check:
integer=int(input("enter your integer: "))
if integer==0:
    print(f"{integer} is zero.")
elif str(integer)[0]=="-":
    print(f"{integer} = negative.")
else:
    print(f"{integer} = positive.")


#percentage:
physics=int(input("enter marks obtained out of 100:"))
chemistry=int(input("enter marks obtained out of 100:"))
biology=int(input("enter marks obtained out of 100:"))
mathematics=int(input("enter marks obtained out of 100:"))
computers=int(input("enter marks obtained out of 100:"))
MO=(physics+biology+mathematics+computers+chemistry)
percentage=((MO/500)*100)
print(percentage)
if percentage>=90:
    print("grade=A")
elif 80<=percentage<90:
    print("grade=B")
elif 70<=percentage<80:
    print("grade=C")
elif 60<=percentage<70:
    print("grade=D")
elif 40<=percentage<60:
    print("grade=E")
elif percentage<40:
    print("grade=F")


#triangle:
side1=input("enter the length of the first side of the triangle: ")
side2=input("enter the length of the second side of the triangle: ")
side3=input("enter the length of the third side of the triangle: ")
if side1==side2==side3:
    print("it is an equilateral triangle. ")
elif side2==side1 or side1==3 or side2==side3:
    print("it is an isosceles triangle.")
else:
    print("it is a scalene triangle.")


#email:
E_mail="abc@gmail.com"
password="abc"
Input_E_mail=input("Enter E-mail: ")
if Input_E_mail==E_mail:
    Input_password=(input("enter password: "))
    if password==Input_password:
        print("user logged in.")
    else:
        print("Invalid Password.")
else:
    print("invalid email.")
    

#leap year:
year=int(input("enter year: "))
if (year%4==0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

