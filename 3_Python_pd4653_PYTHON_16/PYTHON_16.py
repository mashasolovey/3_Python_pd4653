import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Przygotowanie danych
proby = ['Proba1', 'Proba2', 'Proba3']
ekspresja = np.array([
    [5.1, 2.3, 7.8],
    [3.2, 4.5, 6.1],
    [4.8, 5.5, 3.9]
])

# Tworzenie wykresów w Matplotlib

# Wykres liniowy
plt.figure(figsize=(8, 6))
plt.plot(proby, ekspresja[0], label='GenA', marker='o', color='r')
plt.plot(proby, ekspresja[1], label='GenB', marker='s', color='g')
plt.plot(proby, ekspresja[2], label='GenC', marker='^', color='b')
plt.title('Zmiany ekspresji genów w próbkach')
plt.xlabel('Próbki')
plt.ylabel('Poziom ekspresji')
plt.legend()
plt.grid(True)
plt.show()

# Wykres słupkowy
plt.figure(figsize=(8, 6))
bar_width = 0.2
index = np.arange(len(proby))

# Wysokości słupków dla każdego genu
bar1 = ekspresja[0]
bar2 = ekspresja[1]
bar3 = ekspresja[2]

plt.bar(index - bar_width, bar1, bar_width, label='GenA', color='r')
plt.bar(index, bar2, bar_width, label='GenB', color='g')
plt.bar(index + bar_width, bar3, bar_width, label='GenC', color='b')

plt.xlabel('Próbki')
plt.ylabel('Poziom ekspresji')
plt.title('Porównanie ekspresji genów w próbkach')
plt.xticks(index, proby)
plt.legend()
plt.show()

# Wykres rozrzutu
plt.figure(figsize=(8, 6))
plt.scatter(ekspresja[0], ekspresja[1], color='purple')
plt.title('Porównanie ekspresji GenA i GenB')
plt.xlabel('Ekspresja GenA')
plt.ylabel('Ekspresja GenB')
plt.grid(True)
plt.show()

# Tworzenie wykresów w Seaborn

# Wykres violin plot
data = {
    'GenA': ekspresja[0],
    'GenB': ekspresja[1],
    'GenC': ekspresja[2]
}

sns.set(style="whitegrid")
plt.figure(figsize=(8, 6))
sns.violinplot(data=data)
plt.title('Rozkład ekspresji genów w próbkach')
plt.ylabel('Poziom ekspresji')
plt.show()

# Wykres pudełkowy (box plot)
plt.figure(figsize=(8, 6))
sns.boxplot(data=data)
plt.title('Rozkład ekspresji genów w próbkach (box plot)')
plt.ylabel('Poziom ekspresji')
plt.show()

# Eksport wykresu
# Wybierz jeden wykres do zapisania, np. wykres słupkowy
plt.figure(figsize=(8, 6))
plt.bar(index - bar_width, bar1, bar_width, label='GenA', color='r')
plt.bar(index, bar2, bar_width, label='GenB', color='g')
plt.bar(index + bar_width, bar3, bar_width, label='GenC', color='b')

plt.xlabel('Próbki')
plt.ylabel('Poziom ekspresji')
plt.title('Porównanie ekspresji genów w próbkach')
plt.xticks(index, proby)
plt.legend()

# Zapisz wykres do pliku PNG
plt.savefig('ekspresja_genow.png')

