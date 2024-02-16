# #WHILE LOOP:
# #print a string 10 times using for loop.
# for i in range(11):
#     print("programming is fun!")
# #print a string 10 times using while loop.
# i=0
# while i<11:
#     print("programming is fun!")    #11 is the sentinal value.
#     i+=1

# #take 2 numbers print the numbers and their sums:
# n1=int(input("enter number here: "))
# n2=int(input("enter number here: "))
# i=0
# while i<3:
#     print(f"{n1}+{n2}={n1+n2}")
#     i+=1

# #BREAK:
# #store sum of variables in a a variable sum.
# sum=0
# n3=0
# while n3<5:
#     n3+=1
#     sum+=n3
#     if sum==10:    
#         break        #it wont add 5 to the sum.the last loop.
# print(n3)       #the last number added.
# print(sum)      #the sum gotten by adding the last number i.e 4.


#CONTINUE:
sum1=0
n4=0
while n4<20:
    n4+=1
    if n4==10 or n4==11:         #we skip adding 11 and 10 in sum.
        continue
    sum1+=n4
print(sum1)

# #Example: Skip even numbers in a loop

# for i in range(1, 11):
#     if i % 2 == 0:          # Skip the rest of the code inside the loop for even numbers
#         continue
#     print(i,end=" ")

# #SUM PRINT WITH EVAL AND WHILE:
# data=int(input("enter an integer: "))
# sum=0
# while data!=0:
#    sum+=data
#    data=int(input("enter an integer: "))
# print(f"the sum is {sum}")


# #FOR LOOPS:
# #just a list:
# for i in range(1,8):
#     print(i)

# #skip(slice):
# for j in range(1,11,2):
#     print(j)

# #index reversal:
# for k in range(5,1,-1):
#     print(k)

# #NESTED LOOPS:
# #multiplication table:
# for i in range(6,7):
#     for y in range(1,11):
#         z=i*y
#         print(f"{i}*{y}={z}")
#prime numbers:
for i in range(2,11):
    c=0
    for j in range(2, i):
        if i%j==0:
            c+=1
    if c==0:
        print(i, end=" ")


# #SLIDE 20(DEC)
# i=5
# while i>=1:
#     num=1
#     for j in range(1,i+1):
#         print(num,end="xxx")
#         num*=2
#     print()
#     i-=1

for i in range(2,11):
    c=0
    for k in range(2,i):
        if i%k==0:
          c+=1
    if c==0:
          print(i,end=" ")

       






    
