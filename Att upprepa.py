gissa = input("Skriv gissning")

gissa = float(gissa)

while gissa != 5:
    print("fel")
    if gissa <5:
        print("för litet")
    elif gissa >5:
        print("more!")
print("51")