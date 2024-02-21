# A = int(input("Enter the rows: "))
# for i in range(A):
#     for j in range(i+1):
#         print("*",end="")
#     print()
# for i in range(A):
#     for j in range(A):
#         print(" ",end="")
#     for j in range(A):
#         print("*",end="")
#     for j in range(i+1):
#         print("*",end="") 
#     print()
# for i in range(A):
#     for j in range(2*A+5):
#         print(" ",end="")
#     for j in range(2*A):
#         print("*",end="")
#     for j in range(i+1):
#         print("*",end="")
#     print()

# t=int(input("enter your rows: "))
# for i in range(t):
#     for j in range(i+1):
#         print("*",end="")
#     print()
# for i in range(t):
#     for j in range(t):
#         print(" ",end="")
#     for j in range(t):
#         print("*",end="")
#     for j in range(i+1):
#         print("*",end="")
#     print()
# for i in range(t):
#     for j in range(3*t):
#         print(" ",end="")
#     for j in range(2*t):
#         print("*",end="")
#     for j in range(i+1):
#         print("*",end="")
#     print()


# l1=[]
# num=int(input("enter your number: "))
# for i in range(1,num):
#     if num%i==0:
#         l1.append(i)
# l2=int(sum(l1))
# if l2==num:
#     print(f"{num} is a perfect number.")
# else:
#     print(f"{num} is not a perfect number.")


# l1=[]
# for i in range(3):
#     num=int(input("enter your number: "))
#     l1.append(num)
# if l1[1]==l1[2]==l1[0]:
#         print(3)
# elif l1[0]==l1[1] or l1[1]==l1[2] or l1[0]==l1[2]:
#     print(2)
# elif l1[0]!=l1[1] and l1[1]!=l1[2] and l1[0]!=l1[2]:
#     print(1)

# l2=[]
# l1=[6,9,6,23,12,19,14,26]
# for i in l1:
#      if l1.count(i)==1:
#           l2.append(i)
# print(l2)


# def vowels(x):
#     sum=0
#     for i in x:
#         if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
#             sum+=1
#     print(f"vowels:{sum}")
        
# def consonants(x):
#     c=0
#     b=x.replace(" ","")
#     for i in b:
#         if i!="a" and i!="e" and i!="i" and i!="o" and i!="u":
#             c+=1
#     print(f"consonants:{c}")
# vowels("i like pakistan")
# consonants("i like pakistan")

balls=int(input("enter number of balls: "))
a=0
b=0
c=0
y=int(input("enter your standard size: "))
for i in range (balls):
    size=int(input("enter your size: "))
    if size==y:
        a+=1
    elif size==2*y:
        b+=1
    elif size>(2*y):
        c+=1
print(f"red balls: {a}")
print(f"blue ball: {b}")
print(f"greeen ball: {c}")


# balls = int(input("Enter number of balls: "))
# bag = []

# for i in range(balls):
#     size = int(input("Enter the size: "))
#     your_size = int(input("Enter your size: "))

#     if size == your_size:
#         a = "Red ball"
#         bag.append(a)
#     elif size == 2 * your_size:
#         b = "Blue ball"
#         bag.append(b)
#     elif size > 2 * your_size:
#         c = "Green ball"
#         bag.append(c)

# print("Number of balls in the bag:", len(bag))

# list2=[]
# list=[1,2,2,2,2,1,3,1,3,3,3,1,5,5,5,0]
# for i in list:
#     if list.count(i)>=4:
#         list2.append(i)
# print(list2)
# c=0
# for i in range(len(list2)):
#     if list2[i]==list2[i-1]:
#         c=c+1
# print(c)

# list=[]
# for i in range(101):
#     if i%2!=0:
#         list.append(i)
# a=len(list)
# for i in range(a):
#     print(f"({list[i]},{list[i+1]})")
#     if i==a-2:
#         break








          
          





