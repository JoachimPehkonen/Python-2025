oikea = 3120
yritys = 0

while True:
    pin = int(input("Syötä PIN-koodi: "))
    yritys += 1

    if pin == oikea:
        if yritys == 1:
            print("PIN-koodi oikein")
        break
    else:
        print("PIN-koodi väärin, syötä PIN uudelleen")
        