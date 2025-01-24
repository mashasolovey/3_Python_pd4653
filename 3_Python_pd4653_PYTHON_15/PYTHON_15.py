import pandas as pd
import numpy as np

# 1. Utwórz DataFrame z danymi ekspresji genów
dane = {
    'Gen': ['GenA', 'GenB', 'GenC', 'GenD'],
    'Proba1': [5.1, 2.3, np.nan, 4.4],
    'Proba2': [3.2, 4.5, 3.9, np.nan],
    'Proba3': [6.3, 5.6, np.nan, 6.6]
}

# 2. Utwórz DataFrame
df = pd.DataFrame(dane)

# 3. Sprawdź, które wartości w DataFrame są brakujące (NaN) i wyświetl wynik
print("Missing values in DataFrame:")
print(df.isna())

# 4. Usuń wiersze z brakującymi danymi i wyświetl nowy DataFrame
df_dropped = df.dropna()
print("\nDataFrame after dropping rows with missing values:")
print(df_dropped)

# 5. Uzupełnij brakujące dane za pomocą średnich wartości dla każdej kolumny i wyświetl wynikowy DataFrame
# Zastosuj fillna tylko do kolumn z wartościami liczbowymi
df_filled = df.copy()
df_filled[['Proba1', 'Proba2', 'Proba3']] = (
    df[['Proba1', 'Proba2', 'Proba3']].fillna(df[['Proba1', 'Proba2', 'Proba3']].mean()))
print("\nDataFrame after filling missing values with mean values:")
print(df_filled)

# 6. Wyciągnij dane dotyczące genu 'GenA' i wyświetl je
genA_data = df[df['Gen'] == 'GenA']
print("\nData for GenA:")
print(genA_data)

# 7. Oblicz średnią ekspresję genów dla każdej z próbek i wyświetl wynik
average_expression = df[['Proba1', 'Proba2', 'Proba3']].mean()
print("\nAverage expression for each sample:")
print(average_expression)

# 8. Filtrowanie: Wyświetl wszystkie geny, których ekspresja w próbce 1 wynosi więcej niż 4
genes_above_4 = df[df['Proba1'] > 4]
print("\nGenes with expression > 4 in Proba1:")
print(genes_above_4)

# 9. Zapisz wynikowy DataFrame (po uzupełnieniu brakujących wartości) do pliku CSV o nazwie 'wynik.csv' bez indeksów
df_filled.to_csv('wynik.csv', index=False)
print("\nThe resulting DataFrame has been saved to 'wynik.csv'.")