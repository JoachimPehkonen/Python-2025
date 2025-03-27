päivä = int(input("Syötä päivä: "))
kuukausi = int(input("Syötä kuukais: "))
vuosi = int(input("Syötä vuosi: "))

#Kuukaudet, jotka päättyy 31 päivään
if kuukausi == 1 or kuukausi == 3 or kuukausi == 5 or kuukausi == 7 or kuukausi == 8 or kuukausi == 10 or kuukausi == 12:
    if 1 <= päivä <= 31:
        print("Päivämäärä on kelvollinen")
    else:
        print("Päivämäärä ei ole kelvollinen")


#Kuukaudet, jotka päätty 30 päivään
elif kuukausi == 4 or kuukausi == 6 or kuukausi == 9 or kuukausi == 11:
    if 1 <= päivä <= 30:
        print("Päivämäärä on kelvollinen")
    else:
        print("Päivämäärä ei ole kelvollinen")

#Karkausvuosi
elif kuukausi == 2:
    if (vuosi % 4 == 0 and (vuosi % 100 != 0 or vuosi % 400 == 0)) and 1 <= päivä <=29:
        print("Päivämäärä on kelvollinen")
    elif 1 <= päivä <= 28:
        print("Päivämäärä on kelvollinen")
    else:
        print("Päivämäärä ei ole kelvollinen")
else: 
    print("Päivämäärä ei ole kelvollinen")
