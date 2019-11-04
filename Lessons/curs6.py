# def function(a,b="Mihaita"):
#     print("My name is",b+".",a+".")

# function("Manda Mihaita","Cristian")    

# def convertor_euro_ron(a, b=4.74):
#     print("Suma in lei este...",b*a)
    
# a=float(input("Suma euro..:"))
# convertor_euro_ron(a)

# def convertor_ron_euro(a, b=4.74):
#     print("Suma este...",a/b,"euro",end=".")
    
# a=float(input("Suma lei..:"))
# convertor_ron_euro(a)


# def adevar (adevar = True):
#     print("Adevarat ?")
#     if not adevar:
#         return
    
#     print("Este adevarat!")

# # adevar(True) 
# adevar(False)

# def none_funct(n):
#     if n % 2 == 0 :
#         return True  

# print(none_funct(4))
# print(none_funct(3)) 

# def intro (firstname,lastname):
#     return(firstname,lastname)

# print(intro("Mihaita","Manda"))
# 
# factorial
# n!-> 1*2*3*4*5*.....*n
# 3!= 1*2*3 = 6
#
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# n=int(input("Insert factorial:"))
# print(factorial(n))

def factorial(n):
    fact=1
    for i in range (1,n+1):
        fact=fact*i
    return fact
n=int(input("Insert factorial:"))
print(factorial(n))

# import math
# print (math.factorial(5))
    

        
    