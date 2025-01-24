#zadanie 4

#Bakterie
bacteria1, bacteria2, bacteria3 = 'E.coli', 'S.cerevisae', 'S.aureus'
print(bacteria1, bacteria2, bacteria3)

#ilość bakterii na płytkach agarowych
colonies1, colonies2, colonies3 = 4,6,0
print(f"{bacteria1} {colonies1} colonies")
print(f"{bacteria2} {colonies2} colonies")
print(f"{bacteria3} {colonies3} colonies")

#suma bakterii na płytkach
suma = colonies1 + colonies2 + colonies3
print (f"Suma bakterii na płytkach wynosi {suma}")

#typy zmiennych
print (type(bacteria1), type(colonies1))


