import re

a = input()
x = re.search("^ab.+$", a)
if(x):
    print("Yes!")

else :
    print("No!")