class Masina():   #clasa de baza

    __marca = None    #variablia privata
    __putere = None
    __nr_usi = None
    __tip_motor = None
    __culoare = None

    def __init__(self, marca, putere, nr_usi, tip_motor, culoare):
        self.__marca = marca
        self.__putere = putere
        self.__nr_usi = nr_usi
        self.__tip_motor = tip_motor
        self.__culoare = culoare
    
    def print(self):
        print("Masina", self.__marca, "are o putere de", self.__putere, "CP, un numar de", 
        self.__nr_usi, "usi, motor pe", self.__tip_motor, "si culoare", self.__culoare, end = " ")

    def set_marca(self, new_mark):

        self.__marca = new_mark

    def get_culoare(self):
        return self.__culoare

class SUV(Masina):
    
    __garda_sol = None

    def __init__(self, marca, putere, nr_usi, tip_motor, culoare, garda_sol):
        Masina.__init__(self, marca, putere, nr_usi, tip_motor, culoare)  #initializator constructor... arata ce mosteneste de la clasa de baza.
        self.__garda_sol = garda_sol

    def print(self):
        Masina.print(self)
        print("iar garda la sol este de", self.__garda_sol,"cm")


a = Masina("Audi", 180, 5,"benzina","verde")
a.print()
print()
'''
print(a.get_culoare())
a.print()'''

b = SUV("ARO", 85, 5, "benzina", "rosie", 30)
b.print()

