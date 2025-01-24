#Utwórz listę zawierającą elementy: ['A', 'T', 'G', 'C', 'A', 'T', 'G', 'G'] oraz krotkę zawierającą zasady
#azotowe: ('Adenina', 'Tymina', 'Cytozyna', 'Guanina').

nucleotides_list = ['A', 'T', 'G', 'C', 'A', 'T', 'G', 'G']
bases = ['Adenine', 'Thymine', 'Cytosine', 'Guanine']

#Wydrukuj pierwszy i ostatni element listy oraz krotki, używając odpowiednich indeksów.
print(f"First element of the nucleotide: {nucleotides_list[0]}")
print(f"Last element of the nucleotide: {nucleotides_list[-1]}")
print(f"First element of the bases: {bases[0]}")
print(f"Last element of the bases: {bases[-1]}")

#Zmodyfikuj jeden z elementów listy, przypisując mu nową wartość. Zwróć uwagę, że krotki są
#niemutowalne i tego nie można zrobić.
nucleotides_list[3] = 'U'
print(f"Modified nucleotide: {nucleotides_list}")

# element na końcu listy za pomocą metody append().
nucleotides_list.append('U')
print(f"Nucleotide after appending 'U': {nucleotides_list}")

#Skorzystaj z pętli for, aby przejść przez wszystkie elementy zarówno listy, jak i krotki, i je wydrukować.
print("\nElements in the nucleotide:")
for nucleotide in nucleotides_list:
    print(nucleotide)

print("\nElements in the bases:")
for base in bases:
    print(base)

#Skorzystaj z list comprehension, aby utworzyć nową listę na podstawie istniejącej, np. zmieniając
#wszystkie litery na małe.
lowercase_list = [nucleotide.lower() for nucleotide in nucleotides_list]
print(f"List with lowercase letters: {lowercase_list}")

