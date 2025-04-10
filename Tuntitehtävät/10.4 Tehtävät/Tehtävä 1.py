ikä = int(input("Ikäsi: "))

if ikä == 0 or ikä == 150:
    print("Virheellinen ikä!")
elif ikä < 6:
    print("Esikoululainen")
elif ikä == 14:
    print("Haastava ikä")
elif ikä >= 16 and ikä <= 18:
    print("Lähes aikuinen")
elif ikä > 18 and ikä < 30:
    print("Olet täysi-ikäinen, muttet vielä keski-iän kriisissä")
elif ikä >= 30 and ikä < 45:
    print("Olet keski-iässä")
elif ikä > 45 and ikä < 65:
    print("Vielä ehtii ennen eläkettä!")
else:
    print("Olet eläkeläinen")