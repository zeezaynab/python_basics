#sqaure:
symbol=input("enter symbol: ")
n=int(input("enter a number: "))
for j in range (n): #incrimant by 1
  for i in range(n):
    print(symbol,end=" ")
  print() #after the inner loop is complete the programme goes back to the outer loop where j(rows) incrimants by 1.

#Rectangle:
symbol5=input("enter symbol: ")
rows=int(input("enter no. of rows: "))
columns=int(input("enter no. of columns: "))
for j in range(rows):
  for i in range(columns):
     print(symbol5,end=" ")
  print() 

#inc right angle triangle pattern:
symbol3=input("enter symbol here: ")
s=5
for j in range(s):
  for i in range(j+1):   #incrimant values of j(rows) by 1.
    print(symbol3,end=" ")
  print()

#dec right angle triangle pattern:
symbol2=input("enter symbol here: ")
r=5
for j in range(r):
  for i in range(j,r):  #values from j(rows) to i(range value input).
    print(symbol2,end=" ")
  print()

#right sided triangle:
w=5
symbol4=input("enter symbol here: ")
for j in range(w):
  for i in range(j,w):
    print(" ",end=" ")
  for i in range(j+1):
    print(symbol4,end=" ")
  print()

#hillside triangle:
s=5
symbol6=input("enter symbol here: ")
for i in range(s):
    for j in range(i,s):
        print(" ",end=" ")
    for j in range(i+1):
        print(symbol6,end=" ")
    for j in range(i):
        print(symbol6,end=" ")
    print()

#REVERSE HILL:
u=5
symbol9=input("enter symbol: ")
for j in range(u):
    for i in range(j+1):
        print(" ",end=" ")
    for i in range(j,u):
        print(symbol9,end=" ")
    for i in range(j,u-1):
         print(symbol9,end=" ")
    print()
        

#diamond:
t=5
symbol8=input("enter symbol: ")
for i in range(t-1):         # minus 1 here to get pointy diamond.
   for j in range(i,t):
      print(" ",end=" ")
   for j in range(i+1):
      print(symbol8,end=" ")
   for j in range(i):             #minus
      print(symbol8,end=" ")
   print()
for j in range(t):
    for i in range(j+1):
        print(" ",end=" ")
    for i in range(j,t):
        print(symbol8,end=" ")
    for i in range(j,t-1):       #minus
         print(symbol8,end=" ")
    print()
      
  
