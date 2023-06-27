sentencepiece with 22M text file > Precision: 0.2625968992248062 Recall: 0.23918799646954986 F-score: 0.25034642032332566

sentencepiece with about 13M text file -> Precision: 0.26522593320235754 Recall: 0.2383053839364519 F-score: 0.2510460251046025



I did mecab word segmentation with bochan.txt and used it to train sentencepiece. I got Precision: 0.24645030425963488 Recall: 0.2144748455428067 F-score: 0.2293534686172723
With plain bochan.txt, I got Precision: 0.25074925074925075 Recall: 0.22153574580759047 F-score: 0.23523898781630742
No big difference. 


large japanese corpus is from livedoor news https://www.rondhuit.com/download.html#ldcc



For apertium-jpn, there is a python file called modCov.py. It tokenize text file with tokeniser.py and evaluation is calculated with untokenized/total. 
It got 42.22% with Hiroshima file. On tests file, python3 modCov.py ~/Desktop/gsoc/apertium-jpn/jpn.automorf.bin ~/Desktop/gsoc/jpn-corpus/Hiroshima_Peace_Park_Wikipedia.txt output the accuracy.

For sentence.py, I simply tried word segmentation aspect and used Hiroshima file as an input. It produces model and vocaburary. With the model, i tokenized Hiroshima file and i got 62.11% with some words from lexc file in apertium-jpn.
word segmentation doc in python https://pypi.org/project/sentencepiece/
I got 85.24% with bochan.txt input. Larger corpus input will make accuracy better.

Brief summary of Sentencepiece:'SentencePiece' solves problem by using 'subwords'. First, the text is split into words and the frequency of each word is determined. High frequency words are then treated as a single vocabulary, while low frequency words are split into shorter vocabulary words. The splitting is then repeated until the vocabulary number reaches a pre-specified number. This makes it possible to eliminate unknown words while keeping the vocabulary size small.


For speed comparison, I used bochan.txt, which is fairly large japanese corpus. I got initinal speed with only one japanese word. 

Below is screenshot of sentencepiece word segmentation(62%)

![Screenshot from 2023-06-22 09-03-49](https://github.com/yypy22/gsoc_try/assets/99264752/e9615d7a-4eac-4845-abaf-d12327a9a828)

Below is with 85% one
![Screenshot from 2023-06-23 00-44-55](https://github.com/yypy22/gsoc_try/assets/99264752/d5f456b4-c0f7-4001-aca7-6a3d8464b37a)
