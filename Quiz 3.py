#EVAL:
print(eval("5**2"))    #since eval hai "" dont matter.
#/ AND //:
print(20/12)           #float mein division ka ans deta.
print(20//12)          #int mein division ka answer deta.
#QUESTION:
for i in range(4):
     cer=input("enter your chararcter: ")
     zer=cer.lower()
     ver=cer.upper()
     ber=cer.isdigit()
     if ber:
         print("input is a digit.")
     elif cer.isalpha():
         if cer==zer:
             print("input is lowercase.")
         elif cer==ver:
             print("input in uppercase.")
     else:
         print("entry is a symbol.")
#ISALPHA():
q="weerty ert"
print(q.isalpha())