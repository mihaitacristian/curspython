class Angajat():
    __departament = None
    __vechime = None

    def __init__(self,departament,vechime):
        self.__departament = departament
        self.__vechime = vechime
    def print(self):
        print("Departamentul",self.__departament,"vechime",self.__vechime)

    def set_departament(self,departament):
        self.__departament = departament
    def set_vechime(self,vechime):
        self.__vechime = vechime
    def get_departament(self):
        return self.__departament
    def get_vechime(self):
        return self.__vechime


class HR(Angajat):
    __nume = None
    __salariu_lunar = None
    __spor = None

    def __init__(self,departament,vechime,nume,salariu_lunar,spor):
        Angajat.__init__(self,departament,vechime)
        self.__nume = nume
        self.__salariu_lunar =salariu_lunar
        self.__spor = spor
    
    def print(self):
        print("Numele este",self.__nume,"salariul lunar este",self.__salariu_lunar,"Spor",self.__spor,end= " ")        
        Angajat.print(self)
        
    def salariu_anual(self):
        return (self.__salariu_lunar * 12) 

    def salariu_total(self):
        if float(self.get_vechime())> 5:
            print(self.salariu_anual()+float(self.__spor))
        else:
            print (self.salariu_anual())    

class Software(Angajat):
    __nume = None
    __salariu_lunar = None
    __spor = None

    def __init__(self,departament,vechime,nume,salariu_lunar,spor):
        Angajat.__init__(self,departament,vechime)
        self.__nume = nume
        self.__salariu_lunar =salariu_lunar
        self.__spor = spor
    
    def print(self):
        print("Numele este",self.__nume,"salariul lunar este",self.__salariu_lunar,"Spor",self.__spor,end= " ")        
        Angajat.print(self)
        
    def salariu_anual(self):
        return (self.__salariu_lunar * 12) 

    def salariu_total(self):
        if float(self.get_vechime())> 5:
            print(self.salariu_anual()+float(self.__spor))
        else:
            print (self.salariu_anual())









# a = Angajat("HR",6)
# a.print()
# print()

# b= HR("HR",6,"iONUT",1200,600)
# b.print()
# print()
# print(b.salariu_anual())
# b.salariu_total()
b= HR("HR",3,"iONUT",1200,600)
b.print()
print()
print(b.salariu_anual())
b.salariu_total()