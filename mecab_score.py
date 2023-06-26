import nltk
import MeCab

#nltk.download("punkt")
from nltk.metrics import precision, recall, f_measure

def calculate_f_score(corpus, output_text):
    # Calculate precision, recall, and F-score
    precision = nltk.precision(set(corpus), set(output_text))
    recall = nltk.recall(set(corpus), set(output_text))
    f_score = nltk.f_measure(set(corpus), set(output_text))
    print("Precision:", precision)
    print("Recall:", recall)
    print("F-score:", f_score)
    #return precision, recall, f_score

with open('non_notation.txt') as f, open('full_annotation.txt') as f1:
    text = f.read()
    text1 = f1.read().split()   # split on spaces!
    a = len(text)
    wakati = MeCab.Tagger("-Owakati")
    b = wakati.parse(text).split()  
    print(b)
    calculate_f_score(b, text1)
    f.close()
    f1.close()
