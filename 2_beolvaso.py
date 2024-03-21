f=open("olvasando.txt","r")
adatok1=f.read()
f.close()
print(adatok1)


f=open("olvasando.txt","r")
adatok2=[]
i = 'x'
while i!='' : 
    i=f.readline()[:-1í]
    adatok2.append(i)

f.close()    
print(adatok2)


hazai = [i for i in adatok2[0].split()]
deli = [i for i in adatok2[1].split()]
primek = [int(i) for i in adatok2[2].split()]
print(hazai)
print(deli)
print(primek)
