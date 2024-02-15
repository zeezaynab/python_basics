#STRINGS:

#REPLACE:
sr="hog"
print(sr.replace("h","l"))
#concatanation:
first=input("name: ")
last=input("name: ")
age= int(input("enter age: "))
print("My name is",first, last,". ", "i am ", age)

#FIND
str=" hello world! "
print(str.find("o")) #returns index
print(str.find("p")) #replies with -1 when entry not found

#COUNT
print(str.count("o")) #returns the number of times something was mentioned.
print(str.count("p")) #replies with 0.

#STRIP
print(str.lstrip())
print(str.rstrip())
print(str.strip())

#ASCII CONVERSIONS:
char="a"
print(ord("a"))

#JOIN:
str2="hello"
str3="-"        
print(str3.join(str2))

#SLICING(start:stop:step):
s="ba zinga"
s2=s[0::2]
print(s2)
s3=s[::-1]
print(s3)

#UPPER LOWER:
a="inggy bingy"
print(a.upper())

#length:
print(len(a))

#index:
print(a[1])

#title:
print(a.title())

#TEST:(index,slicing)
s="water loo"
s2=s[0:5]
s3=s[6:]
s4=s2[::-1]
s5=s3[::-1]
print(f"{s4}{s5}")

#TEST2:
str1="Zainab"
str2="Tariq"
print(str1+" "+str2)

#TEST3:
str="ba zinga"
a=str[3:]
print(a)
print(a[::-1])


