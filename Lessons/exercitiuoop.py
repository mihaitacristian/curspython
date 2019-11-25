class Calculator():
    __marca = None
    __an_fabricatie = None
    __sistem_operare = None
    __memorie_hard = None
    __memorie_ram = None

    def __init__ (self,marca,an_fabricatie,sistem_operare,memorie_hard,memorie_ram):
        self.__marca = marca
        self.__an_fabricatie = an_fabricatie
        self.__sistem_operare = sistem_operare
        self.__memorie_hard = memorie_hard
        self.__memorie_ram = memorie_ram

    def print(self):
            print("Marca calculatorului este ",self.__marca,"anul de fabricatie este",self.__an_fabricatie,".","Are sistemul de operare",self.__sistem_operare,"cu memoria hard ",self.__memorie_hard ,"si memoria ram",self.__memorie_ram ,end=" ")

    def set_marca(self,marca):
        self.__marca = marca
    def set_an_faricatie(self,an_fabricatie):
        self.__an_fabricatie = an_fabricatie
    def set_sistem_operare(self,sistem_operare):
        self.__sistem_operare = sistem_operare
    def set_memorie_hard(self,memorie_hard):
        self.__memorie_hard = memorie_hard
    def set_memorie_ram(self,memorie_ram):
        self.__memorie_ram = memorie_ram        

    def get_marca(self):
        return self.__marca
    def get_an_fabricatie(self):
        return self.__an_fabricatie
    def get_sistem_operare(self):
        return self.__sistem_operare
    def get_memorie_hard(self):
        return self.__memorie_hard
    def get_memerie_ram(self):
        return self.__memorie_ram 

class Laptop(Calculator):  #class clasamostenitoare(clasa de baza):
    __display = None
    __pret = None

    def __init__(self,marca,an_fabricatie,sistem_operare,memorie_hard,memorie_ram,display,pret):
        Calculator.__init__(self,marca,an_fabricatie,sistem_operare,memorie_hard,memorie_ram)
        self.__display = display
        self.__pret = pret
    def print (self):
        Calculator.print(self)
        print ("Display",self.__display,"si costa",self.__pret,end=" ")

    # def set_display(self,display):
    #     self.__display = display
    # def set_pret(selft,pret):
    #     self.__pret = pret
    # def get_display(self):
    #     return self.__display
    # def get_pret(self):
    #     return self.__pret



# a = Calculator("Dell",2019,"windows 10",100,16) 
# a.print()
# print(a)

b = Laptop("Dell",2019,"windows 10",100,16,"full-hd",3000)
b.print()
# print(b)