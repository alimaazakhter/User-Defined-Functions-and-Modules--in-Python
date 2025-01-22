#Recursion in Python 
#(It is mathematical concept, means the funtion can call itself and giving us benifit of looping , They make the code clean and organised)

# Factorial Program 
def fact(n):
    if n == 1:
        return 1
    else:
        return (n*fact(n-1))

print(fact(5))
