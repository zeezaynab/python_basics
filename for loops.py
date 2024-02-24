#**FOR LOOPS**
colour_list=("red","orange","green")
for color in colour_list:
    print(color)
    for i in color:
        print(i)
        if(i=="d"):
            print("damascus")


numbers=(1,"2",3,4.0,5/2,6)
for i in numbers:
    if isinstance (i,int):     #isinstance checks data type
     print("this is a number")
    else:
      print("this is eww")

#range() =>gives a list of numbers

for x in range(3):
  for k in range(0,7):
    print(k+1,end="-")
  print()                #to put the ittterations in different lines.

rows=int(input("enter no. of rows here: "))
colomns=int(input("enter no. of coloums here: "))
symbol=input("enter a symbol to use: ")

for x in range(rows):
  for k in range(colomns):
    print(symbol,end=" ")
  print() 



for x in range(2,24):
  is_prime=True
  for i in range(2,x):
    if x%i==0:
     is_prime=False
  if is_prime:
    print(f'{x} is a prime number')
  else:
    print(f'{x} is not a prime number')
   

