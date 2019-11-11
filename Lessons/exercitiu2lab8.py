# Sa se scrie un program care:

# Creeaza o clasa:
		
# 	1. Angajat
# 		a. nume, varsta, departament
# 		b. o functie salariu_anual care face calculul salariu anual in functie de departament ( vezi dictionar )
# 		c. afisare

# Creeaza un dictionar:
	
# 	1. Salariu_Departament
# 		a. keys - nume departament
# 		b. values - salariu

# Sa se instantieze 6 obiecte de tip angajat ( cu caracteristici diferite ) si sa se afiseze datele necesare despre ele.

salariu_departament = {
    "IT":3000,
    "HR":4000,
    "LOCAL_SUPPORT":1500

}


class Angajat:

    nume = None
    varsta = None 
    departament = None 

    def __init__(self,nume,varsta,departament):
        self.nume = nume
        self.varsta = varsta
        self.departament = departament
    
    
    def afisare (self):
        print("Numele angajatului ete",self.nume,"cu varsta de",self.varsta,"in departamentul",self.departament)
    def salariu_anual(self,salariu):
        return salariu*12
    
angajat1 = Angajat("Ion",24,"IT")
angajat2 = Angajat("Vasile",30,"HR")
angajat3 = Angajat("Ion",18,"LOCAL_SUPPORT")
angajat4 = Angajat("Ion",31,"IT")
angajat5 = Angajat("Ion",19,"LOCAL_SUPPORT")
angajat6 = Angajat("Ion",26,"HR")

angajat1.afisare()
print (angajat1.salariu_anual(salariu_departament[angajat1.departament]))    