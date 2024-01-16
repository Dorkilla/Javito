import Auto

def beolvasas():
    kocsilista=[]
    beFajl= open("auto.txt", "r", encoding="utf-8")
    soraim=beFajl.readlines()
    for index in range(0,len(soraim),1):
        aktsor=soraim[index].strip()
        peldany=Auto.Auto(aktsor[0],aktsor[1],aktsor[2])
        kocsilista.append(peldany)
    beFajl.close()
    return kocsilista

def korszam(kocsilista):
    print("III/Kor:")
    print("\t",end="")

def flotta(kocsilista):
    print("III/Flotta:")
    print("\t", end="")

def ertekes(kocsilista):
    print("III/Értékes")
    print("\t", end="")
    maxIndex=0
    for index in range(0,len(kocsilista),1):
        if kocsilista[index].ev > kocsilista[maxIndex].ev:
            maxIndex=index
    print(f"A legöregebb autó: {kocsilista[maxIndex].ev}")
    return maxIndex


def fajlba_ir(kocsilista):
    kiFajl= open("ki.txt", "w", encoding="utf-8")
    print("ki.txt", file=kiFajl)
    kiFajl.close()

def harmadik():
    kocsilista=beolvasas()
    korszam(kocsilista)
    flotta(kocsilista)
    ertekes(kocsilista)
    fajlba_ir(kocsilista)
