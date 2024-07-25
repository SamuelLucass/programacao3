'''
# em trabalho, algoritmo iterativo

def fibonacci_iterativo(n):
    a,b = 0,1
    for i in range (n):
        a,b = (b,a+b)
        return a
    
print (fibonacci_iterativo(5))
'''
#algoritmo recursivo de fibonacci 
def fibonacci(n):
    if n <= 2:
        return 1
    else:
        return fibonacci (n-1) + fibonacci (n-2)
    
print (fibonacci(3))