#przykład 5

#Zdefiniowanie zmiennej przechowującej sekwencję DNA jako ciąg znaków (str)
Dna_seq = "ATCGTATCTG"
print (type(Dna_seq))

#Wyświetlenie wartości zmiennej i jej typu w jednej linijce
print (f"Dna sequence {Dna_seq}, Type {type(Dna_seq)}")

#Konwersja typu tej zmiennej na listę (list)
dna_list = list(Dna_seq)
print (dna_list)

#Ponowne wyświetlenie wartości zmiennej i jej typu
print (f"Dna sequence {dna_list}, Type {type (dna_list)}")

#Dodatkowo przemyśl czy możesz użyć w jakimś kontekście w tym programie funkcji range().
x = len(dna_list)
print (range (x))
