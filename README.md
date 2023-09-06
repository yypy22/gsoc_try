Final eval draft for 12/09/2023 https://docs.google.com/document/d/1yxQH6hk-_fjIM9U0fx14OcezMwBUcIlM2WC-AM8O5Y8/edit publicly accessble

Encoding one is written above. 

Interjection added

$ cat sample.txt |apertium-destxt|apertium -f none -d .  jpn-morph|apertium-cleanstream -n |grep -F '*'|sort|uniq -c |sort -nr

Nice amount of sample corpus on horror

https://kikikaikai.fan/feature_article/syarekowa/%e3%82%b3%e3%83%88%e3%83%aa%e3%83%90%e3%82%b3

$ cat article.txt | apertium -d .  jpn-disam | cg-conv -a　　　　　　　　　　　　　　　　

$ cat ../gsoc_try/top.txt |apertium-destxt|apertium -f none -d .  jpn-morph|apertium-cleanstream -n |grep -F '*'|sort|uniq -c |sort -nr

I use this https://tool.konisimple.net/text/hinshi_keitaiso 
to understand a part of speech classification types like noun, verb, suffix, etc...

Eng rlx file has 650 lines and for Jpn rlx I will set the goal to have it. 

I will focus on rlx file more from now on. I need to find many samples to see ambiguous words.

With Stay Hungry, Stay Foolish Japanese Script, I got

total words:3299
unknown words:83
coverage: 97.48%


English words are added from https://englishgrammarhere.com/speaking/100-english-sentences-used-in-daily-life/

Probably lexc file can be decreased the words. It does not very properly follow the format MeCab tokenize. 

Created a pull request

Their company names too

British royal names are added and Forbes rich people are added as well

tokenize.py on jpn is fixed 

malformed input error with tokenize.py occurs

English names are added a bit like Tom in katakana form

Some English words are added and I will add them more 

I am adding katakana words from https://benritecho.com/katakanakotoba/ 

After adding normal often used words from non-notation.txt, i got 

total words:2927
unknown words:218
coverage: 92.55%


I added many characters from all-four.txt and it is not too reliable now, so I tried with non-notation.txt.(non-annotation is right name, notation is typo hehe)

total words:2927
unknown words:264
coverage: 90.98%


total words:2016
unknown words:21
coverage: 98.96%

98.96% cover with a new evaluation python file, which just calculates nums of unknown words and divides it with the total num words count.

with all-four.txt, output has these unknown words

![Screenshot from 2023-08-03 14-40-19](https://github.com/yypy22/gsoc_try/assets/99264752/8c3ee123-84aa-4323-b175-98a70b2e7d05)

65% cover is due to * assigned to　の；に；は；を；へ；だ ...etc and modCov.py recognese words with * as unknown words!

test coverage with modCov.py ->need to get modified in tokenized function

business words added into lexc file as katakana character like アサイン

rlx file improved a bit 

![Screenshot from 2023-08-01 15-06-48](https://github.com/yypy22/gsoc_try/assets/99264752/d5909460-0df5-4ab9-909f-57fc9fac67a5)

Goal: corpus coverage over 90%

A bit hard to convert this into rule ![ダウンロード](https://github.com/yypy22/gsoc_try/assets/99264752/b1cbb2ac-5cd4-44e2-89e2-3b6a44bb4299)

Will keep on improving lexc file and rlx file to use tagger and morph command

With new rlx, 
![Screenshot from 2023-07-28 12-54-42](https://github.com/yypy22/gsoc_try/assets/99264752/c42f767c-8631-40d4-8273-eb87039a7c6e)

With old one, as you can see とび is ambiguous here
![Screenshot from 2023-07-28 13-01-26](https://github.com/yypy22/gsoc_try/assets/99264752/60b4cea2-103c-4815-b5e4-3e500f4f6906)

Now
![Screenshot from 2023-07-23 05-49-53](https://github.com/yypy22/GSoC2023/assets/99264752/136f1959-d3e9-4036-a4bd-30f3e67091b8)

After
![Screenshot from 2023-07-22 10-07-13](https://github.com/yypy22/gsoc_try/assets/99264752/64156047-19ce-4865-ad1a-b0a9ec607e2e)

Before
![Screenshot from 2023-07-22 10-06-33](https://github.com/yypy22/gsoc_try/assets/99264752/24f43ee8-2adc-484e-baac-70917ee5160b)

Dictionary Conversion to lexc file research https://docs.google.com/document/d/1p2qFp1g9OufeL_Obgg8vpljfgAwKz4D2briQvqepsMw/edit

real_tokenizer.cpp and mecab_tokenizer.py are moved into apertium-jpn as buffer_mecab.cpp and tokenize.py

C++ file with hfst command 
![Screenshot from 2023-07-12 05-59-04](https://github.com/yypy22/gsoc_try/assets/99264752/487ac8ea-ce7b-46e7-9edf-f48a126b5edd)

tokenizer with hfst command 
![Screenshot from 2023-07-12 05-52-36](https://github.com/yypy22/gsoc_try/assets/99264752/77667f6b-8504-4640-be5b-854fda4bc039)

Slight improvement in tokenize.cpp
![Screenshot from 2023-07-08 12-21-11](https://github.com/yypy22/gsoc_try/assets/99264752/9aede42c-1aa7-43eb-945c-f06cb9b8d583)

tokenizer with mecab in C++
![Screenshot from 2023-07-08 10-16-09](https://github.com/yypy22/gsoc_try/assets/99264752/0e5e1fd0-8f73-4d28-8a28-88480a3afc0a)
a few mistakes seen but working main function well
(tokenize.cpp)

tokenizer with mecab and [] is not processed
![Screenshot from 2023-07-08 05-24-06](https://github.com/yypy22/gsoc_try/assets/99264752/91195902-b791-4680-8879-49e5e9258c5a)
(tokenizer_mecab.py)

tokenize_mecab.py for testing.
probably something still going wrong 
![Screenshot from 2023-07-07 12-23-44](https://github.com/yypy22/gsoc_try/assets/99264752/12e02cba-b68a-4e31-aa56-ec7a609ecf80)



From https://qiita.com/taku910/items/fbaeab4684665952d5a9 
I tried the output file with mecab format and i got Precision: 0.25633528265107214 Recall: 0.2321270962047661 F-score: 0.24363131079203335 with bochan.txt. The command I used was: mecab -F"%M||||" -E"\n" -b 100000 < bochan.txt  > bochan.txt.tok

sentencepiece with 251MB text file from wikipedia japanese data > Precision: 0.357958872810358 Recall: 0.4148278905560459 F-score: 0.384300899427637
probably not best choice for apertium.
It exceeds 100MB and i cannot upload it here. The text look like this
![Screenshot from 2023-07-01 05-56-32](https://github.com/yypy22/gsoc_try/assets/99264752/34032204-a5e4-43d7-ac13-39964f37bdc0)


sentencepiece with 22MB text file > Precision: 0.2625968992248062 Recall: 0.23918799646954986 F-score: 0.25034642032332566 (with 8000 vocab > Precision: 0.357958872810358 Recall: 0.4148278905560459 F-score: 0.384300899427637)

sentencepiece with about 13MB text file -> Precision: 0.26522593320235754 Recall: 0.2383053839364519 F-score: 0.2510460251046025



I did mecab word segmentation with bochan.txt and used it to train sentencepiece. I got Precision: 0.24645030425963488 Recall: 0.2144748455428067 F-score: 0.2293534686172723
With plain bochan.txt, I got Precision: 0.25074925074925075 Recall: 0.22153574580759047 F-score: 0.23523898781630742
No big difference. 


large japanese corpus is from livedoor news https://www.rondhuit.com/download.html#ldcc



For apertium-jpn, there is a python file called modCov.py. It tokenize text file with tokeniser.py and evaluation is calculated with untokenized/total. 
It got 42.22% with Hiroshima file. On tests file, python3 modCov.py ~/Desktop/gsoc/apertium-jpn/jpn.automorf.bin ~/Desktop/gsoc/jpn-corpus/Hiroshima_Peace_Park_Wikipedia.txt output the accuracy.

For sentence.py, I simply tried word segmentation aspect and used Hiroshima file as an input. It produces model and vocaburary. With the model, i tokenized Hiroshima file and i got 62.11% with some words from lexc file in apertium-jpn.
word segmentation doc in python https://pypi.org/project/sentencepiece/
I got 85.24% with bochan.txt input. Larger corpus input will make accuracy better.

Brief summary of Sentencepiece:'SentencePiece' solves problem by using 'subwords'. First, the text is split into words and the frequency of each word is determined. High-frequency words are then treated as a single vocabulary, while low frequency words are split into shorter vocabulary words. The splitting is then repeated until the vocabulary number reaches a pre-specified number. This makes it possible to eliminate unknown words while keeping the vocabulary size small.


For speed comparison, I used bochan.txt, which is fairly large japanese corpus. I got initinal speed with only one japanese word. 

Below is the screenshot of sentence piece word segmentation(62%)

![Screenshot from 2023-06-22 09-03-49](https://github.com/yypy22/gsoc_try/assets/99264752/e9615d7a-4eac-4845-abaf-d12327a9a828)

Below is with 85% one
![Screenshot from 2023-06-23 00-44-55](https://github.com/yypy22/gsoc_try/assets/99264752/d5f456b4-c0f7-4001-aca7-6a3d8464b37a)
