from itertools import cycle
from random import randint
from calendar import monthrange

def createPESEL():
    YourYear = int(input("Podaj rok urodzin:"))
    while YourYear > 2299 or YourYear < 1800:
        YourYear = int(input("Podaj poprawny rok urodzin:"))

    YourMonth = int(input("Podaj miesiąc urodzin:"))
    while YourMonth > 12 or YourMonth < 0:
        YourMonth = int(input("Podaj poprawny miesiąc urodzin:"))
    DaysInMonth = monthrange(YourYear, YourMonth)

    YourDay = int(input("Podaj dzień urodzin:"))
    while YourDay < 0 or YourDay > DaysInMonth[1]:
        YourDay = int(input("Podaj poprawny dzień urodzin:"))

    YourSex = str(input("Podaj płeć[K/M]:"))
    while YourSex != "K" and YourSex != "M":
        YourSex = str(input("Podaj poprawną płeć[K/M]:"))

    if YourSex == "K":
        YourSex = randint(0, 9)
        while YourSex % 2 != 0:
            YourSex = randint(0, 9)

    if YourSex == "M":
        YourSex = randint(0, 9)
        while YourSex % 2 == 0:
            YourSex = randint(0, 9)

    YourSex = str(YourSex)
    #key is the first part of year, value is the value which we need to add to third and fourth number in PESEL
    YearDict = {18: 80, 19: 0, 20: 20, 21: 40, 22: 60}
    YourYear = str(YourYear)
    #First two numbers in PESEL
    YourYearA = str(int(YourYear[2:4]))
    YourYearMonth = int(YourYear[0:2])
    YourYearMonth = str(YearDict[YourYearMonth])
    YourMonth = str(int(YourMonth) + int(YourYearMonth))

    if int(YourMonth) < 10:
        YourMonth = '0' + YourMonth

    if int(YourDay) < 10:
        YourDay = str('0' + str(YourDay))

    if YourYearA == '0':
        YourYearA = '00'

    YourDay = str(YourDay)
    #if result would have value = 10 then PESEL will be count 12 numbers
    result = 10

    while result == 10:
        # 6, 7, 8 number in PESEL
        YourRand = str(randint(100, 999))
        PESEL = YourYearA + YourMonth + YourDay + YourRand + YourSex
        #creating the control/last number in PESEL
        weight = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
        PESELAsList = list(map(int, PESEL))
        result = 0
        for i in range(len(weight)):
            result += weight[i] * PESELAsList[i]
        result = 10 - result % 10

    PESEL = PESEL + str(result)

    return PESEL


print(createPESEL())