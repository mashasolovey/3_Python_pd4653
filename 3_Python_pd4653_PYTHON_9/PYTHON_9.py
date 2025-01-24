# Utwórz zbiór zawierający unikalne elementy oraz słownik, w którym kluczami są nazwy genów, a wartościami ich funkcje
genes_set = {'TP53', 'BRCA1', 'EGFR', 'KRAS'}
genes_functions = {'TP53': 'Tumor suppressor', 'BRCA1': 'DNA repair', 'EGFR': 'Cell signaling'}

# Dodaj nowy element do zbioru oraz nową parę klucz-wartość do słownika
genes_set.add('MYC')
genes_functions['MYC'] = 'Transcription factor'

# Sprawdź, czy określony element istnieje w zbiorze oraz czy klucz znajduje się w słowniku, korzystając z operatora in
print('TP53' in genes_set)
print('BRCA1' in genes_functions)

# Usuń jeden z elementów ze zbioru, korzystając z metody remove() lub discard()
genes_set.remove('KRAS')

# Wyświetl zawartość słownika: klucze oraz wartości za pomocą iteracji pętli for
for gene, function in genes_functions.items():
    print(f"{gene}: {function}")

# Skorzystaj z instrukcji warunkowej if-else, aby sprawdzić długość zbioru. Jeśli zawiera więcej niż 3 elementy, wydrukuj odpowiedni komunikat
if len(genes_set) > 3:
    print("Set has more than 3 genes.")

# Skorzystaj z instrukcji warunkowej, aby sprawdzić, czy określony klucz istnieje w słowniku i, jeśli tak, wyświetl jego wartość
if 'EGFR' in genes_functions:
    print(f"Function EGFR: {genes_functions['EGFR']}")

# Przeprowadź operację łączenia zbiorów (za pomocą metody union()), a następnie wydrukuj wynik
another_set = {'BRCA2', 'CDKN2A'}
union_set = genes_set.union(another_set)
print(f"Sets connect: {union_set}")