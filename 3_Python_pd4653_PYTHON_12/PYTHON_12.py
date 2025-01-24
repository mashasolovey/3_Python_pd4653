# Otwórz plik zawierający sekwencje DNA i odczytaj jego zawartość
# Program powinien otworzyć plik tekstowy zawierający sekwencje DNA (np. sequences.txt) i odczytać jego zawartość.
# Jeśli plik nie istnieje, program powinien obsłużyć ten błąd (FileNotFoundError) i poinformować użytkownika o problemie.
try:
    with open("sequences.txt", "r") as file:
        dna_sequence = file.read()
        print(f"DNA sequence from file: {dna_sequence}")
except FileNotFoundError:
    print("Error: The file 'sequences.txt' was not found.")

# Pobierz nową sekwencję DNA od użytkownika
# Poproś użytkownika o podanie nowej sekwencji DNA, którą chciałby zapisać do pliku.
# Sekwencja musi zawierać jedynie litery A, T, C, G. Jeśli użytkownik poda inne znaki, zgłoś błąd (stwórz własny wyjątek, np. InvalidDNASequence).
class InvalidDNASequenceError(Exception):
    pass

def get_dna_sequence():
    sequence = input("Please enter a new DNA sequence (only A, T, C, G): ").upper().strip()  # Strip any extra spaces
    if not all(base in 'ATCG' for base in sequence):
        raise InvalidDNASequenceError("Invalid DNA sequence. Only A, T, C, and G are allowed.")
    return sequence

# Pobierz prawidłową sekwencję DNA od użytkownika
# Zweryfikuj, że sekwencja DNA podana przez użytkownika jest poprawna.
try:
    new_dna_sequence = get_dna_sequence()
except InvalidDNASequenceError as e:
    print(e)
    exit()

# Zapisz nową sekwencję DNA do pliku (nadpisz, jeśli plik już istnieje)
# Program powinien zapisać nową sekwencję DNA podaną przez użytkownika do pliku o nazwie new_sequence.txt.
# Jeśli plik już istnieje, nadpisz jego zawartość.
with open("new_sequence.txt", "w") as file:
    file.write(new_dna_sequence)
    print(f"New DNA sequence saved to 'new_sequence.txt': {new_dna_sequence}")