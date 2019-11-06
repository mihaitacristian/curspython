#Dictionare  {keys:values}

# sala_de_clasa={

#     "culoare": 6,
#     "mese": 6,
#     "scaune": 22,
#     "ferestre": 6,
#     "prize" : "putine",
#     "becuri": 9,
#     "tabla": 1,
#     "cos_de_gunoi": "are",
#     "studenti": "da",
#     "mocheta": "una mare"
# }



# # print(len(sala_de_clasa))
# # print(sala_de_clasa.keys())
# # print(sala_de_clasa.values())
# # print(sala_de_clasa)
# print(sala_de_clasa["becuri"])

# for element in sala_de_clasa.keys():
#         print(element,sala_de_clasa[element],sep=":")

# sala_de_clasa["plante"]="fara"
# sala_de_clasa["wi-fi"]="nu sunt fonduri"
# sala_de_clasa["creta"]="este"
# sala_de_clasa["culori"]="da"
# sala_de_clasa["nr. elevi clasa"]= 20

# for key in sala_de_clasa.keys():
#     for value in sala_de_clasa.values():
#         print(key,value)

# sala_de_clasa2={
    
#     "culoare": 6,
#     "mese": 6,
#     "scaune": 22,
#     "ferestre": 6,
#     "prize" : "putine",
#     "becuri": 9,
#     "tabla": 1,
#     "cos_de_gunoi": "are",
#     "studenti": "da",
#     "mocheta": "una mare"
# }

# sala_de_clasa2["profesor"]=["ALIN","ILIE","COSMIN","FLORIN"]
# # print(sala_de_clasa2)

# print(sala_de_clasa2["profesor"])
# print(sala_de_clasa2["profesor"][0])
# print(sala_de_clasa2["profesor"][1])
# print(sala_de_clasa2["profesor"][2])

# for key in sala_de_clasa2.keys():
#     for value in sala_de_clasa2:
#         print(key,sala_de_clasa2["profesor"])


magazine = {
    "filiala": ["Buziasului", "Torontalului"],
    "tura" : ["zi","noapte"],
    "zi": ["luni", "marti", "miercuri", "joi", "vineri"],
    "depozit" : ["A123","B432"],
    "nr_angajati_tura" : [5, 2],
    "inventar" : [True , False],
    "non-stop": True

}

for element in magazine.keys():
    print(element,magazine[element],sep=":")
    
print(magazine["depozit"][1],magazine["tura"][1],magazine["filiala"][1])
# print(magazine["tura"][1])
# print(magazine["filiala"][1])