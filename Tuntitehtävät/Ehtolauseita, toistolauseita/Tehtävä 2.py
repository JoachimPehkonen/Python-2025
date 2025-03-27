luku1 = int(input("Syötä ensimmäinen luku: "))
luku2 = int(input("Syötä toinen luku: "))
luku3 = int(input("Syötä kolmas luku: "))
print(f"Syötä kolme lukua:{luku1} {luku2} {luku3}")

if luku1 >= luku2 and luku1 >= luku3:
    suurin = luku1
    if luku2  >= luku3:
        keski = luku2
        pienin = luku3
    else: 
        keski = luku3
        pienin = luku2
elif luku2 >= luku1 and luku2 >= luku3:
    suurin = luku2
    if luku1 >= luku3:
        keski = luku1
        pienin = luku3
    else:
        keski = luku3
        pienin = luku1
else:
    suurin = luku3
    if luku1 >= luku2:
        keski = luku1
        pienin = luku2
    else:
        keski = luku2
        pienin = luku1

print(f"Järjestys: {pienin}, {keski}, {suurin}")