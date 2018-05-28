from itertools import cycle
from random import randint

def validate_pesel(PESEL):
    weight = [1, 3, 7 ,9, 1 ,3 ,7 ,9 ,1 , 3]
    PList = list(map(int, PESEL))
    Control = PList.pop(len(PList)-1)
    result = 0
    for i in range(len(weight)):
        result += weight[i] * PList[i]
    result = 10 - result % 10
    if result == Control:
        if int(PList[9]) % 2 == 0:
            plec = "K"
        else:
            plec = "M"

        if int(PList[3]) == 8 or int(PList[3]) == 9:
            rok = "18"
            miesiac = int(PESEL[2:4]) - 80
        elif int(PList[3]) == 2 or int(PList[3]) == 3:
            rok = "20"
            miesiac = int(PESEL[2:4]) - 20
        elif int(PList[3]) == 0 or int(PList[3]) == 1:
            rok = "19"
            miesiac = int(PESEL[2:4]) - 60
        elif int(PList[3]) == 4 or int(PList[3]) == 5:
            rok = "21"
            miesiac = int(PESEL[2:4]) - 40
        else:
            rok = "22"
        dzien = int(PESEL[4:6])
        miesiac = int(PESEL[2:4])
        rok = rok + str(PESEL[0:2])
        print(rok)

    return "Twój pesel jest poprawny, urodziłeś się {}.{}.{} i Twoja płeć to {}".format(dzien, miesiac, rok, plec)


