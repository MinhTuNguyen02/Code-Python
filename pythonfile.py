import re
s=input()
x=re.findall('.py$',s)
if x:
    print("yes")
else:
    print("no")
