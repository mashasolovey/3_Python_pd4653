# Importing Counter from collections to count nucleotides
from collections import Counter

# Function to return a basic description of the cell
def opis_komorki():
    return "Komórka to podstawowa jednostka życia."

# Function to count nucleotides in a given DNA sequence
def licz_nukleotydy(sekwencja):
    return Counter(sekwencja)
