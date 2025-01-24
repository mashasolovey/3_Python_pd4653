import ssl
from Bio import Entrez


ssl._create_default_https_context = ssl._create_unverified_context

from Bio import Entrez, SeqIO
from Bio.Align import PairwiseAligner
import warnings


warnings.filterwarnings("ignore", category=UserWarning, module="Bio")


# pobieranie sekwencji z GenBanku
def fetch_sequence_from_genbank(accession_id):
    Entrez.email = "solovianova.mariia@gmail.com"  # Podaj swój adres e-mail
    handle = Entrez.efetch(db="nucleotide", id=accession_id, rettype="gb", retmode="text")
    record = SeqIO.read(handle, "genbank")
    handle.close()
    return record


#  zapisywanie sekwencji do pliku FASTA
def save_to_fasta(records, filename):
    SeqIO.write(records, filename, "fasta")


#  porównanie sekwencji z wykorzystaniem algorytmu Needleman-Wunsch
def align_sequences(seq1, seq2):
    aligner = PairwiseAligner()
    aligner.mode = 'global'  # Ustawienie trybu na globalne dopasowanie
    alignments = aligner.align(seq1.seq, seq2.seq)  # Dopasowanie globalne
    best_alignment = alignments[0]  # Wybór najlepszego dopasowania
    return best_alignment


# program
if __name__ == "__main__":
    # Pobierz sekwencje z GenBanku
    seq1 = fetch_sequence_from_genbank("JX669568")
    seq2 = fetch_sequence_from_genbank("JX669571")

    # Zapisz sekwencje do pliku FASTA
    save_to_fasta([seq1, seq2], "sequences.fasta")

    # Wczytaj sekwencje z pliku FASTA
    records = SeqIO.parse("sequences.fasta", "fasta")
    seq1_fasta = next(records)
    seq2_fasta = next(records)

    # Porównaj sekwencje za pomocą Needleman-Wunsch
    alignment = align_sequences(seq1_fasta, seq2_fasta)

    # Wyświetl wynik najlepszego dopasowania oraz punktację
    print("Dopasowanie:")
    print("Punkty:", alignment.score)  # Punktacja dopasowania
    print("Sekwencja 1:", alignment[0])
    print("Sekwencja 2:", alignment[1])
