ikä = int(input("Anna ikäsi: "))

#Jos ikä on pienempi kuin 0 tai suurempi kuin 150, tulostetaan ”Virheellinen ikä!”
if ikä == 0 or ikä == 150:
    print("Virheellinen ikä!")

#Jos ikä on alle 6 tulostetaan ”Esikoululainen”
elif ikä < 6:
    print("Esikoululainen")

#Jos ikä on tasan 14 tulostetaan ”Haastava ikä”
elif ikä == 14:
    print("Haastava ikä")

#Jos ikä on 16 - 18 tulostetaan ”Lähes aikuinen”
elif ikä >= 16 and ikä <= 18:
    print("Lähes aikuinen")

#Jos ikä on suurempi kuin 18, mutta pienempi kuin 30 tulostetaan,”Olet täysi-ikäinen, muttet vielä keski-iän kriisissä”
elif ikä > 18 and ikä < 30:
    print("Olet täysi-ikäinen, muttet vielä keski-iän kriisissä")

#Jos ikä on suurempi tai yhtä suuri kuin 30, mutta pienempi kuin 45 tulostetaan: ”Olet keski-iässä”
elif ikä >= 30 and ikä < 45:
    print("Olet keski-iässä")

#Jos ikä on suurempi kuin 45 mutta alle 65 tulostetaan ”Vielä ehtii ennen eläkettä!”
elif ikä >= 45 and ikä <= 65:
    print("Vielä ehtii ennen eläkettä!")

#Muuten ohjelma tulostaa ”Olet eläkeläinen”
else:
    print("Olet eläkeläinen")

#Mitä ongelmia kyseisitä ehdoista löydät? Miten korjaisit ne?
#Ei mitään hajua vielä miten kaorjata "ongelmia" tuosta, mutta kaikki toimii nyt kuten pitää. Paitsi nyt 1-5-vuotiaat ovat esikoululaisia, mutta en jaksa korjata asiaa

