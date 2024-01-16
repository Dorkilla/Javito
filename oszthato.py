import random

def listaLetrehozas():
    print("A lista elemei:")
    szamoklista=[]
    for szam in range(0,50,1):
        vszam=random.randint(1,100)
        szamoklista.append(vszam)
    return szamoklista

def lista_kiir(szamoklista):
    for index in range(0,len(szamoklista)-1,1):
        print(f"{szamoklista[index]},",end="")
    print(szamoklista[len(szamoklista)-1])

def hettelOszthato(szamoklista):
    db=0
    for index in range(0,len(szamoklista)):
        if szamoklista[index]%7==0:
            db+=1
    return db

def konzolra_kiir(db):
    print(f"A 7-tel oszthatók száma: {db}.")

def masodik():
    szamoklista=listaLetrehozas()
    lista_kiir(szamoklista)
    db=hettelOszthato(szamoklista)
    konzolra_kiir(db)


