magazin1 = {
    "mere" : 7,
    "pere" : 8,
    "banane" : 10,
    "gutui" : 12,
    "coniac" : 20,
    "bere" : 15,
    "hartie" : 23
}
magazin2 = {
    "mere" : 9,
    "pere" : 8,
    "banane" : 10,
    "gutui" : 11,
    "coniac" : 20,
    "bere" : 12,
    "hartie" : 23
}
magazin3 = {
    "mere" : 6,
    "pere" : 8,
    "banane" : 9,
    "gutui" : 12,
    "coniac" : 20,
    "bere" : 15,
    "hartie" : 23
}

for key in magazin3.keys():
    for key in magazin1.keys():
        for key in magazin2.keys():
            print(key,":","magazin1",magazin1[key],"magazin2:",magazin2[key],"magazin3:",magazin3[key])


# def functie(produs):
#     if magazin1[produs]<magazin2[produs]:
#         print(produs,"in", "magazin1 e cel mai ieftin")
#     elif magazin1[produs]>magazin2[produs]:
#             print(produs,"in", "magazin2 e mai ieftin")
#     else:
#         print("sunt egale")   


# for element in magazin1:
#     functie(element)
       



    