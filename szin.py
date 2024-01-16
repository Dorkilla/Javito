def elso():
    print("Első feladat:")
    print("\t", end="")
    mod=input("Kérek egy színkeverési módszert:")
    kod=input("\tKérem a kódot:")
    modszerJok="RGB", "HEX", "HSL", "RGBA", "HSLA"
    kodJok=[]
    for kod in range(1,3,1):
        kodJok.append(kod)
    if len[kod]==5 or 6 or 7 or 8 or 9 or 10:
        if kod[0] in modszerJok:
            if int(kod[6]+kod[7]+kod[8]+kod[9]+kod[10])in kodJok:
                if mod=="RGB":
                    print("Megfelelő hossz.")
                else:
                    print("Bonyolult kiszámolni.")
            else:
                print("Bonyolult kiszámolni.")

    elif len[kod]==7 or 8 or 9 or 10 or 11 or 12:
        if kod[0] in modszerJok:
            if int(kod[7]+kod[8] +kod[9] + kod[10] + kod[11] + kod[12]) in kodJok:
                if mod=="HSL":
                    print("Nem megfelelő hossz.")
                else:
                    print("Bonyolult kiszámolni.")
            else:
                print("Bonyolult kiszámolni.")







