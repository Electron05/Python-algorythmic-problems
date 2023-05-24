def ceil(liczba):
    if liczba != liczba // 1:
        liczba = liczba // 1 + 1
    return liczba
def owce(owce):
    konwynik = owce + 1
    okopia = owce
    start = 1
    while okopia > 99:
        start = start * 10
        okopia = okopia // 100
    konI = 0
    if (owce>=100000):
        odstep = start
        wyr = 147000
    elif (owce>50000):
        odstep = start
        wyr = 50000
    else:
        wyr = 2
        odstep =1
    for i in range(start, (owce // 2) + 2, odstep):
        aktwynik = i + ceil(owce / i)
        if (aktwynik < konwynik):
            konwynik = aktwynik
            konI = i
        if (aktwynik > konwynik):
            minus1 = konI
            plus = konI
            minus = konI
            plus1 = konI
            break
    if (odstep > wyr):
        plusback = 0
        minusback = 0
        while True:
            plus = plus + wyr
            aktwynik = plus + ceil(owce / plus)
            if (aktwynik < konwynik):
                konwynik = aktwynik
                plusback = plus
            if (aktwynik > konwynik):
                break
        while True:
            minus = minus - wyr
            aktwynik = minus + ceil(owce / minus)
            if (aktwynik < konwynik):
                konwynik = aktwynik
                minusback = minus
            if (aktwynik > konwynik):
                break
        for i in range(1,3):
            if (i ==1):
                if plusback != 0:
                    plus1 = plusback
                    minus1 = plusback
            else:
                if minusback != 0:
                    plus1 = minusback
                    minus1 = minusback
            while True:
                plus1 = plus1 + 1
                aktwynik = plus1 + ceil(owce / plus1)
                if (aktwynik < konwynik):
                    konwynik = aktwynik
                if (aktwynik > konwynik):
                    break
            while True:
                minus1 = minus1 - 1
                aktwynik = minus1 + ceil(owce / minus1)
                if (aktwynik < konwynik):
                    konwynik = aktwynik
                if (aktwynik > konwynik):
                    break
    elif (odstep > 1):
        while True:
            plus1 = plus1 + 1
            aktwynik = plus1 + ceil(owce / plus1)
            if (aktwynik < konwynik):
                konwynik = aktwynik
            if (aktwynik > konwynik):
                break
        while True:
            minus1 = minus1 - 1
            aktwynik = minus1 + ceil(owce / minus1)
            if (aktwynik < konwynik):
                konwynik = aktwynik
            if (aktwynik > konwynik):
                break
    print(int(konwynik))
owce(int(input()))

