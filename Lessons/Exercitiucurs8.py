# class Monitor:

#     dimensiune: None 
#     culoare: None 
#     display: None

#     def __init__(self,dimensiune,culoare,display):
#         self.dimensiune = dimensiune
#         self.culoare = culoare
#         self.display = display

#     def afisiare_monitor(self):
#         print("In sala exista un display de dimensiunea:",self.dimensiune,"de culoare:",self.culoare,"cu display",self.display)

# monitor1=Monitor(16,"negru","LCD")
# monitor1.afisiare_monitor()

class Rack:

    nr_server = None
    memorie_server = None
    retelistica = None

    def __init__(self, nr_server,memorie_server,retelistica):
        self.nr_server = nr_server
        self.memorie_server = memorie_server
        self.retelistica = retelistica

    def afisare_rack(self):
        print("In sala exista un numare de",self.nr_server,"servers cu capacitatea de ",self.memorie_server,"mb, plus un router de la",self.retelistica)

rack1=Rack(3,100,"Cisco")
rack1.afisare_rack()