# #printing no. :
# n=int(input("enter a number"))
# for x in range (1,n):
#     print (x)

# # 2b)even:
# for i in range(1,15):
#   if i%2==0:
#     print(i)
#   else:
#     i+=1

# # 2a)odd:
# for x in range(1,101):
#    if x%2==0:
#      print(x+1)

# # 3)prime number:
# n=int(input("enter no. : "))
# x=2
# c=0
# for i in (x,n):
#     if n%i==0:
#         c+=1    
#     if c==0:
#         print("prime no.")
#         break
#     else:
#         n=int(input("enter no. :"))


# # 4)TABLES:
# for i in range(1,9):
#    for j in range(1,11):
#       x=j*i
#       print(f"{j}*{i}={x}")

# # 5)Triangle:
n=4
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print(2**(j),end=" ")           #2 ki power j.
    for j in range(i,0,-1):
        print(2**(j-1),end=" ")
    print()

# #CLASSWORK:
    
# #pyramid but like ajeeb:
# r=int(input("enter integer: "))                       #        1
# for i in range(r):                                    #      2 1
#     for j in range(i,-1,-1):                          #    3 2 1 
#         print(j+1,end=" ")                            #  4 3 2 1 
#     print()


# #print sequence:
# rows=int(input("enter rows no.: "))
# for i in range(rows):
#   for x in range(1,10,2):
#     print(x,end=" ")
#   print()


#number pattern
# n=4
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end="")
#     for j in range(i+1):
#         print(i,end=" ")
#     print()