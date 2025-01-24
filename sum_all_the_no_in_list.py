#Write a Python funtion to sum all the numbers in a list.
def add(number):
    total = 0
    for i in number:
        total = total+i
        return(total)
    
print (add([2,3,4,1]))
