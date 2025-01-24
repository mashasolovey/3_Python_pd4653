# Utwórz klasę Organizm, która będzie zawierała nazwę, rodzaj i metodę opisu organizmu.
class Organism:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describe(self):
        return f"Organism name: {self.name}, Type: {self.type}"

    @staticmethod
    def transcribe(dna_sequence):
        return dna_sequence.replace("T", "U")

# Utwórz klasę Bakteria, która dziedziczy po klasie Organizm, dodając atrybut kształt i rozszerzając metodę opisu.
class Bacteria(Organism):
    def __init__(self, name, type, shape):
        super().__init__(name, type)
        self.shape = shape

    def describe(self):
        organism_description = super().describe()
        return f"{organism_description}, Shape: {self.shape}"

# Utworz instancje bakterii i wywołaj metodę opisz.
e_coli = Bacteria("Escherichia coli", "Bacterium", "Rod-shaped")
salmonella = Bacteria("Salmonella", "Bacterium", "Spherical")

print(e_coli.describe())
print(salmonella.describe())

# Zamien DNA na RNA przy użyciu metody statycznej transkrybuj.
dna_sequence = "ATGCATGCATGC"
rna_sequence = Organism.transcribe(dna_sequence)
print(f"DNA sequence: {dna_sequence}, RNA sequence: {rna_sequence}")