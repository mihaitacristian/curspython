#Sa se scrie un program care sa: 
# -creeze 3 dictionare (magazin1,magazin2,magazin3) care sa contina produse(key) si 7 preturi diferite(values) 
# -parcurga toate dictionarele si sa le printeze sub forma key:value
# -parcurga dictionarele si sa afiseze pentru fiecare produs, magazinul in care are pretul minim
# -se verifice(avand in vedere punctul c) care magazin are cele mai ieftine produse

magazin1={
    "mar":10,
    "banana":11,
    "para":15,
    "kiwi":25,
    "rosie":2,
    "castravete":3,
    "varza":5
}
magazin2={
    "mar":11,
    "banana":17,
    "para":18,
    "kiwi":26,
    "rosie":9,
    "castravete":1,
    "varza":4
}
magazin3={
    "mar":13,
    "banana":7,
    "para":16,
    "kiwi":29,
    "rosie":0.5,
    "castravete":3.1,
    "varza":5.5
}

for element1 in magazin1:
    print(element1+":"+str(magazin1[element1]))
print()    
for element2 in magazin2:
    print(element2+":"+str(magazin2[element2]))
print()
for element3 in magazin3:
    print(element3+":"+str(magazin3[element3]))

magazin_ieftin1=0
magazin_ieftin2=0
magazin_ieftin3=0

def functie(produs):
    global magazin_ieftin1
    global magazin_ieftin2
    global magazin_ieftin3
    if magazin1[produs]<magazin2[produs] and magazin1[produs]<magazin3[produs]:
        print("Cel mai mic pret se gaseste in magazinul 1: "+str(magazin1[produs]))
        magazin_ieftin1+=1
        return magazin_ieftin1
        
    elif magazin1[produs]>magazin2[produs] and magazin3[produs]>magazin2[produs]:
        print("Cel mai mic pret se gaseste in magazinul 2: "+str(magazin2[produs]))
        magazin_ieftin2+=1
        return magazin_ieftin2
    elif magazin3[produs]<magazin1[produs] and magazin3[produs]<magazin2[produs]:
        print("Cel mai mic pret se gaseste in magazinul 3: "+str(magazin3[produs]))
        magazin_ieftin3+=1
        return magazin_ieftin3
        

for produs in magazin1:
    functie(produs)

if magazin_ieftin1>magazin_ieftin2 and magazin_ieftin1>magazin_ieftin3:
    print("Magazinul 1 are cele mai ieftine produse!")
elif magazin_ieftin2>magazin_ieftin1 and magazin_ieftin2>magazin_ieftin3:
    print("Magazinul 2 are cele mai ieftine produse!")
elif magazin_ieftin3>magazin_ieftin1 and magazin_ieftin3>magazin_ieftin2:
    print("Magazinul 3 are cele mai ieftine produse!")
elif magazin_ieftin1==magazin_ieftin2:
    print("Magazinul 1 si 2 au cele mai ieftine produse!")
elif magazin_ieftin1==magazin_ieftin3:
    print("Magazinul 1 si 3 au cele mai ieftine produse!")
elif magazin_ieftin2==magazin_ieftin3:
    print("Magazinul 2 si 3 au cele mai ieftine produse!")


     
        
