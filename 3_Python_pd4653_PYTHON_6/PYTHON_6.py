#Zdefiniuj zmienne zawierające przykładowe sekwencje DNA.
sequence1 = "ATGCTCTTTGTCA"
sequence2 = "CTGATCGTCATGATTCA"

#Użyj operacji konkatenacji do połączenia dwóch sekwencji DNA w jedną dłuższą sekwencję
connect = sequence1 + sequence2
print (connect)

# Wytnij fragment tej sekwencji za pomocą string slicing
print (connect[:5]) #pierwsze 5
print (connect[5:]) #po pierwszych 5
print (connect[-5:]) #ostatnie 5
print (connect[3:10]) # od 3 do 9 indeksu

#Skorzystaj z co najmniej dwóch metod na łańcuchach znaków (np. count(), find(), replace() itp.) do
#analizy sekwencji.
connect1 = connect.lower()
print(connect1)
atg_times = connect1.count("atg")
print(atg_times)
connect_rep = connect1.replace("atg","cgt")
print(connect_rep)
print(connect.isdigit())
print (connect.isidentifier())

#Zformatuj wynik, używając przynajmniej jednej z metod formatowania łańcuchów (np. f-string, format()
#lub %).
connect_sep = connect1.split("atg")
print (connect_sep)

#Użyj znaku ucieczki, np. nowej linii \n lub tabulatora \t, aby poprawnie wyświetlić sformatowany wynik na
#ekranie.
result = (
    f"DNA:\n{connect}\n\n"
    f"Fragment replace:\t{connect_rep}\n"
    f"Fragment separate:\t{connect_sep}\n\n"
)
print (result)

