for i in range(4):                                 #          1
    for j in range (i,4):                          #         121
        print(" ",end=" ")                         #        12421
    for j in range(i+1):                           #       1248421
        print(2**j,end=" ")
    for j in range(i,0,-1):
        print(2**(j-1),end=" ")
    print()

for k in range(4):                                 #         1
    for l in range(k+1):                           #         22
        print(k+1,end=" ")                         #         333
    print()                                        #         4444

num=1                                              #         1
for h in range(5):                                 #         3  5
    for j in range(h):                             #         7  9  11
        print(num,end=" ")                         #         13 15 17 19
        num+=2
    print()

n=1
for q in range(5):
    for w in range(q):
        print(n,end=" ")
        n+=1
    print()

for t in range(4):
    for y in range(t+1):
        print("*",end=" ")
    print()
for y in range(3):
    for u in range(y,3):
        print("*",end=" ")
    print()


t=int(input("enter no. : "))
for i in range (t-1):
    for l in range(i,t):
        print(" ",end=" ")
    for l in range(i+1):
        print("*",end=" ")
    for l in range(i):
        print("*",end=" ")
    print()
for i in range(t):
    for l in range(i+1):
        print(" ",end=" ")
    for l in range(i,t):
        print("*",end=" ")
    for l in range(i,t-1):
        print("*",end=" ")
    print()

t=int(input("enter size you want: "))
for i in range(t-1):
    for j in range(i,t):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(t):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,t):
        print("*",end=" ")
    for j in range(i,t-1):
        print("*",end=" ")
    print()


str="zainab"
x=0
for i in str:
    x+=1
    print(str[0:x])
for i in str:
    x=x-1
    print(str[0:x])

x=4
for i in range(x):
    for j in range(i,x):
        print(" ",end=" ")
    for j in range(i+1):
        print(j,end=" ")
    for j in range(i,0,-1):
        print(j,end=" ")
    print()


   

q=int(input("enter no. : "))
for i in range (q-1):
    for j in range(i,q):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(q):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,q):
        print("*",end=" ")
    for j in range(i,q-1):
        print("*",end=" ")
    print()

x=3+5j
y=5j
z=-5j
print(type(x))
print(type(y))
print(type(z))

str="hello world"
i=str.index("d")
print(str[i])