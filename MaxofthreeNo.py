# write a funtion to find maximum of three values 
def maximum_val(val1, val2, val3):
    if val1 > val2 and val1 > val3:
        print(val1,"is the greatest number")
    elif val2 > val1 and val2 > val3:
        print(val2,"is the greatest number")
    else:
        print(val3,"is the greatest number") 

maximum_val(12, 65, 9)
