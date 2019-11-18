 ################# liste #############
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


list1 = [1,6,5,8,9]
lista2 = ["Andra", "Andi","Radu","Alexandra"]
# list1.extend(lista2) # add lista2
list1.append(10) #adauga la final valoarea "10"
list1.sort() #sorteaza lista
list1.reverse()
lista3 = list1.copy() # compiaza list1 in lista 3

print(lista3)
