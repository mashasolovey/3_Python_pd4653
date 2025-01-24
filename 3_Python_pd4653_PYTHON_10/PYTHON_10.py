# Zdefiniuj funkcję charakterystyka_białka, która przyjmuje sekwencję białka, masę oraz punkt izoelektryczny (pI) jako argumenty nazwane.
# Zwróć sformatowany tekst, który opisuje białko, uwzględniając te trzy wartości.
def protein_characteristics(sequence, mass, pI):
    return f"Protein sequence: {sequence}, Mass: {mass} kDa, pI: {pI}"


# Zaimplementuj w tym samym skrypcie funkcję sumuj_cechy_bialek, która przyjmuje dowolną liczbę nazwanych cech białek (masa, pI) za pomocą **kwargs
# i zwraca sumę mas oraz średnią punktu izoelektrycznego.
def sum_protein_features(**kwargs):
    total_mass = 0
    total_pI = 0
    count = 0

    for feature, value in kwargs.items():
        if 'mass' in feature:
            total_mass += value
        elif 'pI' in feature:
            total_pI += value
            count += 1

    average_pI = total_pI / count if count > 0 else 0
    return total_mass, average_pI


# Wywołanie funkcji charakterystyka_białka
protein_description = protein_characteristics('MKTVRQGCLLAA', 50.5, 6.3)
print(protein_description)

# Wywołanie funkcji sumuj_cechy_bialek
total_mass, average_pI = sum_protein_features(mass_1=50.5, pI_1=6.3, mass_2=45.0, pI_2=5.8)
print(f"Total mass: {total_mass} kDa, Average pI: {average_pI}")