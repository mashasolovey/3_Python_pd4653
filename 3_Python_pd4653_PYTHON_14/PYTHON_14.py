import numpy as np

# 1. Utwórz macierz ekspresji
expression_matrix = np.array([
    [5.0, 2.5, 7.0],
    [3.2, 4.0, 6.0],
    [8.1, 9.3, 2.5],
    [4.5, 5.7, 6.9]
])

# 2. Zwiększ ekspresję genów o 5%
expression_matrix_increased = expression_matrix * 1.05
print("Gene expression increased by 5%:")
print(expression_matrix_increased)

# 3. Oblicz średnią ekspresję dla każdego genu
average_expression = np.mean(expression_matrix_increased, axis=1)
print("\nAverage expression for each gene:")
print(average_expression)

# 4. Oblicz sumę ekspresji genów dla każdej próby
sum_expression = np.sum(expression_matrix_increased, axis=0)
print("\nSum of gene expression for each sample:")
print(sum_expression)

# 5. Wprowadź wartości NaN dla brakujących danych
expression_matrix_with_nan = expression_matrix.copy()
expression_matrix_with_nan[1, 2] = np.nan  # Brakująca wartość w drugiej próbie dla drugiego genu
expression_matrix_with_nan[3, 0] = np.nan  # Brakująca wartość w czwartej próbie dla pierwszego genu
print("\nMatrix with NaN values introduced:")
print(expression_matrix_with_nan)

# 6. Oblicz średnią ekspresję, ignorując wartości NaN
average_expression_with_nan_ignored = np.nanmean(expression_matrix_with_nan, axis=1)
print("\nAverage gene expression (ignoring NaN values):")
print(average_expression_with_nan_ignored)