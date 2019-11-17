lista_cumparaturi = {
    "banane" : 2,
    "mere" : 3,
    "gutui" : 4,
    "legume" : 7
}

magazin = {
    "mere" : 10,
    "banane" : 6,
    "gutui" : 8,
    "legume" : 9,
    "deodorant" : 12
}

def suma(produs,pret):
    sum=0
    for produs in lista_cumparaturi:
        for pret in magazin:
            if produs==pret:
                prod=lista_cumparaturi[produs]*magazin[pret]
                sum=sum+prod
    print(sum)

suma(lista_cumparaturi,magazin)
                
