import sentencepiece as spm
import nltk
#nltk.download("punkt")
from nltk.metrics import precision, recall, f_measure

spm.SentencePieceTrainer.Train('--input=bochan.txt --model_prefix=sentencepiece --vocab_size=8000 --character_coverage=0.9995')
sp=spm.SentencePieceProcessor()
sp.Load("sentencepiece.model")

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
    reference = f_ref.read().split()    # split into a list
    output = sp.EncodeAsPieces(text_in) # sp already returns a list
    calculate_f_score(set(reference),
                      set(output))
