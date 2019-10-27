# a=6
# b=3
# a/=2*b
# print(a)
# 5


# if (a > b):
#     print(float(a))

# else:
#     print(float(b))    

# a=input("Insert number a:")
# b=input("Insert number b:")
# if a>b:
#     print(a)
# elif b>a:
#     print (b)
# else:
#     print ("a=b")   
################ exercitiu barman
# nume=input ("Numele clientului: ")
# varsta=input ("Varsta clientului: ")
# if int(varsta)<18:
#     print("nume ","ai varsta sub 18"+"\nPimesti un TEDI")
# elif int(varsta) == 18:
#     print(nume+"Arata-mi buletinu")
# elif int(varsta) >18 and int(varsta)<=20:
#     print(nume,"ce bautura doresti ?")
# elif int(varsta) > 20:
#     print("Orice bautura !!!!")     
####### problema 2

# nume=input("Numele Clientul:") 
# buget=int(input("Buget:"))
# if buget > 50000:
#     print("BMW I8")  
# elif buget == 50000:
#     print("BMW S3")
# elif buget > 70000:
#     print("Dacie tati")
# elif buget >= 2000:
#     print("Golf 3")
# elif buget < 2000:
#     print("Mergi RATT")                 
###########
# salariu=float(input("Salariul tau este ...:"))
# rata=float(input("Rata o sa fie...:"))

# if salariu<rata:
#     print ("Rata este mai mare"+ salariu +"\n","Me home")
# elif salariu>rata:
#     print ("Possible new home")
# elif salariu>rata and salariu>5000:
#     print("Salariul tau este",salariu + "\n"+"Nice hose")    
###############3

# produs=input("Ce fructe doresti:")
# ppf1=input("Ce legume doresti:")
# ppf2=input("Alte fructe doresti:?")
# if produs == "gutui":
#     print("Cumpar")
# elif produs == "mere" and ppf2 == "banane":
#     print ("Le vreau pe amble...") 
# elif produs == "mere" and ppf1 == "cartof" and ppf2 == "banane":
#     print ("Vreau "+produs,"si",ppf2)   
# else:
#     print ("O zi frumoasa va doresc")   
#  ################# liste #############
# a=23
# b=1
# lista=["fruct",-1,a,5,"a","b",8,9] ####lista[start:stop]
# lista1=[]                          ####lista[start:stop:pas] 
# lista1.append(a)
# lista1.append(a+b)
# lista1.append(b)
# lista1.append(lista)
# # # print (lista1)
# # print(lista1[::-1])
# # # print(lista1[:3])
# # # print(lista1[0:3])
# # # print(lista[0:7:2])              ####lista[start:stop:pas] lista[1:3:2]
# # count = lista1.count("b")                                    lista[-1:-3:-2]
# count = len(lista1)
# print(count)
# print(lista[-1:-5:-2]) 

# my_list = ['p','r','o','g','r','a','m','i','z']
# # elements 3rd to 5th
# print(my_list[2:5])
# # elements beginning to 4th
# print(my_list[:-5])
# # elements 6th to end
# print(my_list[5:])
# # elements beginning to end
# print(my_list[:])
# lista1=[1,2,3,4,5,6,7,8,9]
# lista2=[10,11,12,13,14,15]
# lista2.append(lista1)
# lista2.extend(lista1)
# print(lista2)
# print(lista2[6])

courses = ['History','Math','Physic','CompSci']

print(courses)



