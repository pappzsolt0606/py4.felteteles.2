'''
2. Feladat
Készíts egy programot, ami bekér egy számot a felhasználótól, majd kiírja, hogy a megadott szám páros-e vagy páratlan!

[Tipp] A maradékos osztás segít! Mennyivel is kell elosztanod a számot maradékosan, hogy kiderüljön páros-e? Ebben az esetben mennyi lesz a maradék?
'''
szam = int(input('Adj meg egy számot! '))
if szam %2 == 0:
    print(szam)
    print("A megadott szám páros")
else:
    print(szam)
    print("A megadott szám páratlan")
