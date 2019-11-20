# # x =1 
# # print(type(x))

# # lista = [1,2]
# # list.append [3]
# class Cat:
#     kind="feline" #kind atriubut de tip clasa
#     def __init__(self,name):
#         self.name = name #instanta atributte
#         self.__mood=5 # __private atributes
#         self.__hungry = 2
#         self.__energy = 5
#         self.__sleep = 6

#     def feed(self):
#         self.__hungry-=1
#         self.__mood+=1
#         self.__energy+=1
#         print("feeding",self.name)


#     def sleep(self):
#         self.__sleep+=1
#         self.__hungry-=1

#     def meow(self):
#         print("Meow")

#     def play(self):
#         self.__energy-=1
#         self.__hungry+=1
#         self.meow()
    
#     def get_state(self):
#         return "hungry" + str(self.__hungry)


# cat1=Cat("Thomas")
# print(cat1)
# print(cat1.name)
# print("Initial state",cat1.get_state())


class Animal:
    type = ""
    nr_of_legs = 2
    hungry = 3
    def __init__(self,name):
         self.name=name
   
    def feed(self):
        self.hungry -= 1
    def get_status(self):
        return " hungry"  + str(self.hungry)

class Cat(Animal):
    type = "feline"
    nr_of_legs = 4
    def feed(self):  #method.overriding
        self.hungry-=2

class Dog(Animal):
    type = "canine"
    nr_of_legs = 4
    def __init__(self,name): #method.overriding
        self.name = name
        self.tricks=[]
    def learn_trick(self,trick):
        self.tricks.append(trick)

cat1=Cat("Pis")
cat1.feed()

dog1 = Dog("Spike")
dog1.learn_trick("roll over")
print(dog1.tricks)


#inheritance vs composition





