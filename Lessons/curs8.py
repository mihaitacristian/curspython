#####Clase
class Scaun:
    nr_picioare = None
    culoare = None 
    dimensiune = None 

    def __init__(self,nr_picioare,culoare,dimensiune):
            self.nr_picioare=nr_picioare
            self.culoare=culoare
            self.dimensiune=dimensiune
    def afisiare(self):
        print("Scaunul are", self.nr_picioare, "picioare cu o dimensiune de",self.dimensiune,"cm si culoarea",self.culoare)

scaun1=Scaun(4,"galben",100)
scaun2=Scaun(6,"albastru",150) 
scaun3=Scaun(8,"verde",200)   

scaun1.afisiare()