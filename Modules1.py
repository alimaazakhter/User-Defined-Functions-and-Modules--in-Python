#Modules : Modules are the (.py) files, that contains set of functions you want to include in your program.

#DateTime Module :-

import datetime

x = datetime.datetime.now()
print(x)

y = datetime.datetime(1912,10,2)
print(y)
print(y.strftime("%A"))
print(y.strftime("%m"))