

#a = [23, 34, 425, -32, 73, 6, 256, 9, 33, 45.7]

v=[23,11,42,53,48,25,16]
#print("lungimea vectorului este:", len(v[2:4]))
"""for x in v:
    print(x)"""

#sa se afiseze elementele pare din vectorul v
"""for x in v:
    if x % 2 == 0:
        print(x)"""

#sa se afiseze elementele de pe pozitiile impare
"""for i in range(len(v)):
    if i % 2 != 0:
        print(v[i])"""



###Afisare din 2 in 2
""" a = [23, 34, 425, -32, 73, 6, 256, 9, 33, 45.7]
for i in range(0,len(a),2):
    print(a[i])"""

####Afisare elemente fara 0
v = [23, 34, 425, -32, 73, 6, 0, 9, 33, 45.7]
for i in range(len(v)):
    if v[i] == 0:
        continue
    print(v[i])  ####

### sa se opreasca cand ajunge la 0

v = [23, 34, 425, -32, 73, 6, 256, 9, 33, 45.7]
for i in range(len(v)):
    if v[i]== 0:
        break
    print(v[i]) ###


#varianta mai eficienta
"""print()
for i in range(1, len(v), 2):
    print(v[i])"""


