# x =1 
# print(type(x))

# lista = [1,2]
# list.append [3]
class Cat:
    kind="feline" #kind atriubut de tip clasa
    def __init__(self,name):
        self.name = name #instanta atributte
        self.__mood=5 # __private atributes
        self.__hungry = 2
        self.__energy = 5

    def feed(self):
        self.__hungry-=1
        self.__mood+=1
        self.__energy+=1
        print("feeding",self.name)


    def sleep(self):
        self.__sleep+=1
        self.__hungry-=1

    def meow(self):
        print("Meow")

    def play(self):
        self.__energy-=1
        self.__hungry+=1
        self.meow()
    
    def get_state(self):
        return "hungry" + str(self.__hungry)


cat1=Cat("Thomas")
print(cat1)
print(cat1.name)
print("Initial state",cat1.get_state())

