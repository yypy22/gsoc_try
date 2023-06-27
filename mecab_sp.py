
import MeCab
# Read input files
with open('bochan.txt') as f_in, open('full_annotation.txt') as f_ref:
    text_in = f_in.read()
    reference = f_ref.read().split()  # split into a list

# MeCab analysis and conversion to a single string
wakati = MeCab.Tagger('-Owakati')
result = wakati.parse(text_in).split()  # split into a list
my_string = ' '.join(result)
new_string = my_string.replace("。","。\n")

# Save MeCab output to a file
with open('mecab_output_bochan.txt', 'w') as file:
    file.write(new_string)
