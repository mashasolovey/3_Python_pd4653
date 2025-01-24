# Utwórz własny moduł o nazwie biologia.py, który będzie zawierał dwie funkcje:
# - opis_komorki() – funkcja zwróci tekst: "Komórka to podstawowa jednostka życia".
# - licz_nukleotydy(sekwencja) – funkcja przyjmie jako argument sekwencję DNA (ciąg znaków) i
#   zwróci liczbę każdego typu nukleotydu (A, T, C, G), korzystając z modułu collections.Counter.

# Użyj modułu os do utworzenia katalogu o nazwie "dane_bio", a następnie:
# - W tym katalogu utwórz plik nukleotydy.txt, do którego zapiszesz wyniki z funkcji licz_nukleotydy,
#   która zliczy nukleotydy w przykładowej sekwencji DNA: "AGCTTAGCTAAGGCT".

# Użyj modułu datetime do zapisu aktualnej daty i czasu utworzenia pliku w pliku nukleotydy.txt.

# Zaimportuj i użyj modułów biologia, os oraz datetime w swoim głównym programie, aby:
# - Wyświetlić wynik działania funkcji opis_komorki().
# - Zapisać liczbę nukleotydów i aktualny czas utworzenia pliku do pliku nukleotydy.txt.

# Importowanie niezbędnych modułów
import os
import datetime
import biologia

# Wyświetlenie wyniku działania funkcji opis_komorki
print(biologia.opis_komorki())

# Utworzenie katalogu 'dane_bio', jeśli nie istnieje
if not os.path.exists("dane_bio"):
    os.makedirs("dane_bio")

# Przykładowa sekwencja DNA
sekwencja_dna = "AGCTTAGCTAAGGCT"

# Uzyskanie liczby nukleotydów za pomocą funkcji z modułu biologia.py
nukleotydy = biologia.licz_nukleotydy(sekwencja_dna)

# Pobranie aktualnej daty i godziny
current_time = datetime.datetime.now()

# Zapisanie wyników do pliku 'nukleotydy.txt'
file_path = os.path.join("dane_bio", "nukleotydy.txt")
with open(file_path, "w") as file:
    file.write(f"DNA sequence: {sekwencja_dna}\n")
    file.write(f"Nucleotide counts: {nukleotydy}\n")
    file.write(f"File created on: {current_time.strftime('%Y-%m-%d %H:%M:%S')}\n")

print(f"Wyniki zapisano w {file_path}")