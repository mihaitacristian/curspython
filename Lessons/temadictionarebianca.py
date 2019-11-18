# A) Sa se creeze un program care creeaza 3 dictionare:
# 	1. sport departament ( 3 departamente si salariul pe departament )
# 	2. angajat1 ( nume, varsta, departament,salariu_lunar,vechime )
# 	3. angajat2 ( nume, varsta, departament,salariu_lunar,vechime )

# B) Sa se defineasca o functie salariu_luni(salariu_lunar,nr_luni) care calculeaza salariul in functie de nr. de luni dorit
# C) Sa se defineasca o functie salariu_total(salariu_lunar,nr_luni,spor,vechime):	
# 	a. Daca angajatul are o vechime mai mare de 5 ani, i se adauga la salariu un spor
# 	b. In caz contrar, salariul se calculeaza in mod obisnuit, fara spor.

# D) Sa se adauge in dictionar 2 key noi ("salariu_anual" si "salariu_total") calculate prin intermediu functiilor de la punctele B) si C).




spor_departament= {
    "Software" : 150,
    "HR" : 100,
    "Marketing" : 50

}


angajat1={
    "nume" : "Melissa",
    "varsta" : 34,
    "departament" : "Software",
    "salariu_lunar" : 3400,
    "vechime" : 6,
    

}

def salariu_luni(salariu_lunar,nr_luni):
    return salariu_lunar * nr_luni

def salariu_total(salariu_lunar,nr_luni,spor,vechime):
    if vechime > 5:
        return salariu_luni(salariu_lunar,nr_luni) + spor
    else:
        return salariu_luni(salariu_lunar,nr_luni)

angajat1["salariu_anual"]=salariu_luni(angajat1["salariu_lunar"],12)
angajat1["salariu_total"]=salariu_total(angajat1["salariu_lunar"],12,spor_departament[angajat1["departament"]],angajat1["vechime"])

print(angajat1)
"""


"""

angajat2={
    "nume" : "Vlad",
    "varsta" : 44,
    "departament" : "HR",
    "salariu_lunar" : 4500,
    "vechime" : 12,
    

}

angajat2["salariu_anual"]=salariu_luni(angajat2["salariu_lunar"],12)
angajat2["salariu_total"]=salariu_total(angajat2["salariu_lunar"],12,spor_departament[angajat2["departament"]],angajat2["vechime"])

for i in angajat2.keys():
    print(i, angajat2[i], sep=": ")

lista_angajati = []
lista_angajati.append(angajat1)
lista_angajati.append(angajat2)

print(lista_angajati)