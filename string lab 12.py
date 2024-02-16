#Task 1:
str="log"
B=str.replace("l","h")
print(B)

#Task 2:
str2="river"
A=str2[::2]
print(A)

#Task 4:
lst=["hi","ni","ji","ki","mi"]  
lst2=[lst[0],lst[4],lst[3]]
print(lst2)

#Task 3:
stra="abc"
strb="xyz"                  #abc xyz
strc=stra+" "+strb          #0123456
strn=strc[0]+strc[5]+strc[2]+strc[3]+strc[4]+strc[1]+strc[6]
print(strn)
#alternate approach
str1="abc"
str2="xyz"
str3= (f'{str1} {str2}')
print(str3)
temp=str1
str1=str2
str2=temp
print(str1,str2)
new_str1=str1[:2] + str2[2:]
new_str2=str2[:2] + str1[2:]
print(f"{new_str1} {new_str2}")

#activity5:
str9="ASANTAATNASA"
if str9[::-1]==str9:
    print("is a palindrome")
else:
    print("no palindrome")








