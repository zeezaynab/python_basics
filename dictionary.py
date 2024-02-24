roll_no ={"zainab": "045","aaminah":"042","tayyeba":"050"}
print(roll_no["zainab"])
#print(roll_no["zojaja"])      #here its going to throw an error. 
print(roll_no.get("zojaja"))  #here its going to say none.

#empty library
library={}
#input library(nested dictionary)
lib={'book1':{'title':input("enter book name: "),'Author':input("enter author name: "),'published':input("enter publication year: ")},
     'book2':{'title':input("enter book name: "),'Author':input("enter author name: "),'published':input("enter publication year: ")},
     'book3':{'title':input("enter book name: "),'Author':input("enter author name: "),'published':input("enter publication year: ")}}
#update:
library.update(lib)
#output
print(library)




