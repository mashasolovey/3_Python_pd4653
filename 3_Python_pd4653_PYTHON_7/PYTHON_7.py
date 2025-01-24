#Zadeklaruj zmienne typu boolean i przypisz im wartości logiczne na podstawie dowolnych
#warunków, np. czy_sekwencja_dna_aktywna = True.
is_dna_sequence_active = True
is_cell_in_mitosis = False
print("Is DNA sequence active?", is_dna_sequence_active)
print("Is the cell in mitosis?", is_cell_in_mitosis)

#Użyj funkcji bool() do sprawdzenia, czy różne zmienne (np. ciąg znaków, lista, liczba) są puste
#lub nie.
rna_sequence = "AUGC"
is_rna_active = bool(rna_sequence)
print(is_rna_active)
cell_age = 5
is_cell_age_valid = bool(cell_age)
print(is_cell_age_valid)
# Przeprowadź kilka operacji arytmetycznych na liczbach, używając operatorów takich jak +, -, *,
#//, %, oraz wypisz wyniki tych operacji.

bacteria_day1 = 100
bacteria_day2 = 250
bacteria_day3 = 400

total_bacteria = bacteria_day1 + bacteria_day2 + bacteria_day3
print(f"Total bacteria after 3 days: {bacteria_day1} + {bacteria_day2} + {bacteria_day3} = {total_bacteria}")

full_sets_of_bacteria = total_bacteria // 100
print(f"Full sets of 100 bacteria after 3 days: {total_bacteria} // 100 = {full_sets_of_bacteria}")
# Zastosuj operatory przypisania do zmiany wartości istniejących zmiennych.
bacteria_day1 += 50
print(f"Updated bacteria on day 1: {bacteria_day1}")

# Subtraction assignment (-=)
bacteria_day2 -= 30
print(f"Updated bacteria on day 2: {bacteria_day2}")

# Multiplication assignment (*=)
bacteria_day3 *= 2
print(f"Updated bacteria on day 3: {bacteria_day3}")


 #Użyj operatorów porównania, aby porównać wartości zmiennych (np. długości sekwencji DNA)
#i wyświetlić odpowiednie komunikaty.
dna_sequence1 = "ATCGGTA"
dna_sequence2 = "ATCGA"
dna_sequence3 = "AGTCG"

if len(dna_sequence1) == len(dna_sequence2):
    print("DNA sequence 1 and DNA sequence 2 have the same length.")
else:
    print("DNA sequence 1 and DNA sequence 2 have different lengths.")

if len(dna_sequence2) != len(dna_sequence3):
    print("DNA sequence 2 and DNA sequence 3 have different lengths.")
else:
     print("DNA sequence 2 and DNA sequence 3 have the same length.")
