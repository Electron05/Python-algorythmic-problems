n = int(input())
skargi = []
class skarga:
    def __init__(self, kto, kogo, kierunek):
        self.kto = kto
        self.kogo = kogo
        self.kierunek = kierunek

for i in range(n):
    x = [item for item in input().split()]
    if x[2] == 'W':
        skargi.append(skarga(x[1], x[0], 'N'))
    else:
        skargi.append(skarga(x[0], x[1], 'N'))

#sortowanie na budynki
bdki = [[]]
for skarga in skargi:
    notfound = 0
    for bd in bdki:
        if skarga.kto in bd and skarga.kogo in bd:
            bd.append(skarga)
            break
        if skarga.kto in bd and skarga.kogo not in bd:
            bd.append(skarga.kogo)
            bd.append(skarga)
            budyneksave = bd
            bdki.remove(bd)
            for budynek1 in bdki:
                if skarga.kogo in budynek1:
                    for element in budynek1:
                        if element not in budyneksave:
                            budyneksave.append(element)
                    bdki.remove(budynek1)
            bdki.append(budyneksave)
        if skarga.kto not in bd and skarga.kogo in bd:
            bd.append(skarga.kto)
            bd.append(skarga)
            budyneksave = bd
            bdki.remove(bd)
            for budynek1 in bdki:
                if skarga.kto in budynek1:
                    for element in budynek1:
                        if element not in budyneksave:
                            budyneksave.append(element)
                    bdki.remove(budynek1)
            bdki.append(budyneksave)
        if skarga.kto not in bd and skarga.kogo not in bd:
            notfound += 1
    if notfound == len(bdki):
        bdki.append([skarga.kto, skarga.kogo,skarga])
bdki.pop(0)


for bd in bdki:
    i = -1
    while i < len(bd):
        i += 1
        try:
            try:
                x = bd[i].kto
            except:
                bd.remove(bd[i])
                i = i-1
        except:
            break
sortb = [[] for i in range(len(bdki))] #tablica koncowa (budynki>>budynek>>pietra>>nazwiska)
x = 1
for bd in bdki:
    #print("Budynek: ", x)
    zmiany = True# whlie zmiany = False
    while zmiany!= False:
        zmiany = False
        for objekt in bd:
            #print("kto - ",objekt.kto,"na kogo - ", objekt.kogo, objekt.kierunek)
            if len(sortb[bdki.index(bd)]) == 0:
                sortb[bdki.index(bd)].append([objekt.kogo])
                sortb[bdki.index(bd)].append([objekt.kto]) # DODAWANIE NA POCZATEK
                #print(sortb)
                zmiany = True# zmiana = True
            else:
                case = []
                for p in range(len(sortb[bdki.index(bd)])):
                    if objekt.kto in sortb[bdki.index(bd)][p]:
                        ikto = p #index kto
                        case.append(["kto",p])
                    if objekt.kogo in sortb[bdki.index(bd)][p]:
                        ikogo = p #index kogo
                        case.append(["kogo",p])
                try:
                    if ikto < ikogo+1: # DODANIE NOWEGO WARUNKU DLA ISTNIEJĄCYCH JUŻ LOKATORÓW
                        zmiany = True #zmiana = True
                        sortb[bdki.index(bd)][ikogo].remove(objekt.kogo)
                        if ikto !=0:
                            sortb[bdki.index(bd)][ikto - 1].append(objekt.kogo)
                        else:
                            sortb[bdki.index(bd)].insert(0,[objekt.kogo])
                except:
                    zmiany = True#zmiana = True
                    # JEDEN (ZE SKARGI) JEST W BUDYNKU, DRUGI NIE
                    for tab in case:
                        if tab[0] == "kogo": # JEŚLI OSKARŻONY JEST W BUDYNKU
                            sortb[bdki.index(bd)][-1].append(objekt.kto)
                        else: # JEŚLI OSKARŻAJĄCY JEST W BUDYNKU
                            if tab[1] != 0:
                                sortb[bdki.index(bd)][ikto-1].append(objekt.kogo)
                            else:
                                sortb[bdki.index(bd)].insert(0, [objekt.kogo])
                case.clear()
                try:
                    del ikto
                except:
                    pass
                try:
                    del ikogo
                except:
                    pass
                #print(sortb)
    x += 1

dictionaries = []
for a in sortb: # Budynki posortować alfabetycznie!
    i = -1
    dict = []
    while i < len(a):
        i += 1
        try:
            for c in a[i]:
                dict.append([c])
                dict[dict.index([c])].append(sortb[sortb.index(a)].index(sortb[sortb.index(a)][sortb[sortb.index(a)].index(a[i])]))
            if not a[i]:
                a.remove(a[i])
                i -= 1
        except:
            break
    dictionaries.append(sorted(dict))

x = 1
for dict in sorted(dictionaries):
    print("Budynek ",x,": ",sep="")
    for item in dict:
        print(item[0],item[1])
    x += 1