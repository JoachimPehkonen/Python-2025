oikeak = "Käyttäjä"
oikeas = "1234"

while True:
    käyttäjä = input("Syötä käyttäjätunnnus: ")
    salasana = input("Syötä salasana: ")

    if käyttäjä == oikeak and salasana == oikeas:
        print("Oikein meni!")
        break
    else:
        print("Väärin meni, syötä uudelleen")

