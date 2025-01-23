# write a funtion to create and print a list where the values are square of numbers between 1 to 30
def create_list():
    list = []
    for i in range(1,31):
        list.append(i**2)
        
    return list
print(create_list())