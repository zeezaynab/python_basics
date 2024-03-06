# #Q1)PALINDROME CHECKER:
# for i in range(2):
#   string=input("enter your word/phrase here: ")
#   string2=string[::-1]
#   if string2==string:
#        print(f"{string} is a palindrome.")
#   else:
#        print(f"{string} is not a palindrome.")

#Q2)PATTERNS:
#a):
num = 1
for i in range(5):
        for j in range(i):
            print(num,end=" ")
            num += 1
        print()
#b):
i=int(input("enter no. of rows here: "))
for k in range(i):
  for j in range(k+1):
       print(j+1,end=" ")
  print()
  
#c):
for r in range(5):
    for c in range(1,r+1):
        print(r,end=" ")
    print()

#d):
row=5
for i in range(row):
    print("*"*(i+1))
for j in range(row):
    print("*"*(row-j-1))

# #Q3)FUNCTIONS:
# #fibonacci sequence.
# l=[0,1]
# def fibo_seq():
#     x=int(l[-1])
#     y=int(l[-2])
#     z=x+y
#     l.append(z)
#     print(l)
# seq=int(input("enter the number of times you'd like the sequence to be executed: "))
# for i in range(seq):
#   fibo_seq()

# #Q4)
# #RANDOM GUESSING GAME:
# import random
# prompt=input("\nwe'll be giving you a random number abd you have to guess it!\nlets start!")
# number=random.randint(1,5)
# for i in range(6):
#     chosen_number=int(input("enter your number:"))
#     if chosen_number==number:
#         print("yes!you guessed it correctly:D")
#         break
#     elif chosen_number>number:
#         print("guess a litte lower")
#     elif chosen_number<number:
#         print("guess a little higher")






