import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Odczyt sekwencji z pliku
def read_sequences(file_path):
    sequences = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if not line.startswith(">") and is_valid_sequence(line):  # Pomijaj nagłówki FASTA i sprawdzaj poprawność
                    sequences.append(line)
    except FileNotFoundError:
        print(f"Error: File {file_path} does not exist. Creating a new file...")
        with open(file_path, 'w') as file:
            pass  # Tworzy pusty plik
    return sequences



# Dodawanie nowej sekwencji od użytkownika
def add_user_sequence(sequences, file_path):
    while True:  # Powtarzaj do momentu podania poprawnej sekwencji
        user_sequence = input("Give your DNA sequence: ").strip().upper()  # Konwersja na wielkie litery
        if is_valid_sequence(user_sequence):
            if user_sequence not in sequences:  # Sprawdzanie, czy sekwencja już istnieje
                sequences.append(user_sequence)
                with open(file_path, 'a') as file:
                    file.write(user_sequence + "\n")
                print(f"User's sequence added: {user_sequence}")
            else:
                print("Sequence already exists in the file.")
            break  # Wyjście z pętli po dodaniu poprawnej sekwencji
        else:
            print("Invalid sequence! Only A, T, C, G are allowed. Please enter a valid sequence.")
    return sequences


# Sprawdzanie, czy sekwencja zawiera tylko poprawne nukleotydy
def is_valid_sequence(sequence):
    return all(base in 'ATCG' for base in sequence)


# Tworzenie słownika z sekwencjami
def create_sequence_dict(sequences):
    # Słownik z ID i odpowiadającymi sekwencjami
    sequence_dict = {f"Seq_{i+1}": seq for i, seq in enumerate(sequences)}
    return sequence_dict


# Konwersja słownika na DataFrame
def convert_to_dataframe(sequence_dict):
    # Tworzenie DataFrame z dodatkową analizą (długość, GC content)
    data = {
        "Sequence_ID": list(sequence_dict.keys()),
        "Sequence": list(sequence_dict.values()),
        "Length": [len(seq) for seq in sequence_dict.values()],
        "GC_Content": [
            (seq.count('G') + seq.count('C')) / len(seq) * 100 for seq in sequence_dict.values()
        ],
    }
    df = pd.DataFrame(data)
    return df


# Usuwanie duplikatów i wadliwych sekwencji
def clean_dataframe(df):
    # Usuwanie duplikatów
    df = df.drop_duplicates(subset="Sequence").reset_index(drop=True)
    return df


# Wizualizacje
def visualize_data(df):
    # Wykres długości sekwencji
    plt.figure(figsize=(10, 6))
    sns.histplot(df["Length"], bins=10, kde=True, color="blue")
    plt.title("Distribution of Sequence Lengths")
    plt.xlabel("Length")
    plt.ylabel("Frequency")
    plt.show()

    # Wykres zawartości GC
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=df["GC_Content"], color="green")
    plt.title("GC Content Distribution")
    plt.xlabel("GC Content (%)")
    plt.show()

    # Wykres długości vs zawartość GC
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x="Length", y="GC_Content", data=df, color="red")
    plt.title("GC Content vs Sequence Length")
    plt.xlabel("Sequence Length")
    plt.ylabel("GC Content (%)")
    plt.show()


# Główna część programu
if __name__ == "__main__":
    file_path = "sekwencje.txt"  # Ścieżka do pliku

    # Odczyt sekwencji z pliku
    sequences = read_sequences(file_path)

    # Dodanie nowej sekwencji od użytkownika
    sequences = add_user_sequence(sequences, file_path)

    # Tworzenie słownika z sekwencjami
    sequence_dict = create_sequence_dict(sequences)

    # Konwersja do DataFrame
    df = convert_to_dataframe(sequence_dict)

    # Usuwanie duplikatów
    df = clean_dataframe(df)

    # Wyświetlanie DataFrame
    print("\nDataFrame with sequences:")
    print(df)

    # Wizualizacje danych
    visualize_data(df)
