import nltk
import MeCab

#nltk.download("punkt")
from nltk.metrics import precision, recall, f_measure

wakati = MeCab.Tagger("-Owakati")

def calculate_f_score(reference, output_text):
    # Calculate precision, recall, and F-score
    precision = nltk.precision(reference, output_text)
    recall = nltk.recall(reference, output_text)
    f_score = nltk.f_measure(reference, output_text)
    print("Precision:", precision)
    print("Recall:", recall)
    print("F-score:", f_score)
    #return precision, recall, f_score

with open('non_notation.txt') as f_in, open('full_annotation.txt') as f_ref:
    text_in = f_in.read()
    reference = f_ref.read().split()       # split into a list
    output = wakati.parse(text_in).split() # split into a list
    calculate_f_score(set(reference),
                      set(output))
