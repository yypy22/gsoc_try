<after>
echo FIVBバレーボールネーションズリーグ（Volleyball Nations League）は、FIVB（国際バレーボール連盟）が2018年から開催しているバレーボール国際大会である。男子のバレーボール・ワールドリーグと女子のバレーボール・ワールドグランプリを発展的に統合した大会となる。| python3 tokenize.py | hfst-proc jpn.automorf.hfst

^FIVB/*FIVB$ ^バレーボール/バレーボール<n><sg><abs>$ ^ネーションズ/*ネーションズ$ ^リーグ/リーグ<n><sg><abs>$ ^（/（<lpar>/（<spec>$ ^Volleyball/*Volleyball$ ^Nations/*Nations$ ^League/*League$ ^）/）<rpar>/）<spec>$ ^は/は<n><sg><abs>/は<v><ifml><npst>$ ^、/、<cm>/、<spec>$ ^FIVB/*FIVB$ ^（/（<lpar>/（<spec>$ ^国際/国際<n><sg><abs>$ ^バレーボール/バレーボール<n><sg><abs>$ ^連盟/連盟<n><sg><abs>$ ^）/）<rpar>/）<spec>$ ^が/が<n><sg><abs>/が<suff>$ ^2018/2018<num><abs>$ ^年/年<n><sg><abs>/年<suff>$ ^から/から<adj><abs>/から<n><sg><abs>/から<suff>/から<v><ifml><npst>$ ^開催/開催<n><sg><abs>$ ^し/し<n><sg><abs>/し<suff>/し<v><ifml><npst>$ ^て/て<n><sg><abs>/て<suff>/て<v><ifml><npst>$ ^いる/いる<suff>/いる<v><ifml><npst>$ ^バレーボール/バレーボール<n><sg><abs>$ ^国際/国際<n><sg><abs>$ ^大会/大会<n><sg><abs>$ ^で/で<v><ifml><npst>$ ^ある/ある<suff>/ある<v><ifml><npst>$ ^。/。<sent>/。<spec>$ ^男子/男子<n><sg><abs>$ ^の/の<n><sg><abs>/の<v><ifml><npst>$ ^バレーボール/バレーボール<n><sg><abs>$ ^・/・<spec>$ ^ワールド/ワールド<n><sg><abs>$ ^リーグ/リーグ<n><sg><abs>$ ^と/と<n><sg><abs>/と<suff>/と<v><ifml><npst>$ ^女子/女子<n><sg><abs>$ ^の/の<n><sg><abs>/の<v><ifml><npst>$ ^バレーボール/バレーボール<n><sg><abs>$ ^・/・<spec>$ ^ワールド/ワールド<n><sg><abs>$ ^グランプリ/グランプリ<n><sg><abs>$ ^を/*を$ ^発展/発展<n><sg><abs>$ ^的/的<n><sg><abs>/的<suff>$ ^に/に<n><sg><abs>/に<v><ifml><npst>$ ^統合/統合<n><sg><abs>$ ^し/し<n><sg><abs>/し<suff>/し<v><ifml><npst>$ ^た/た<n><sg><abs>/た<suff>/た<v><ifml><npst>$ ^大会/大会<n><sg><abs>$ ^と/と<n><sg><abs>/と<suff>/と<v><ifml><npst>$ ^なる/なる<suff>/なる<v><ifml><npst>$

<before>
echo FIVBバレーボールネーションズリーグ（Volleyball Nations League）は、FIVB（国際バレーボール連盟）が2018年から開催しているバレーボール国際大会である。男子のバレーボール・ワールドリーグと女子のバレーボール・ワールドグランプリを発展的に統合した大会となる。| python3 tokenize.py | hfst-proc jpn.automorf.hfst
  
^FIVB/*FIVB$ ^バレーボール/*バレーボール$ ^ネーションズ/*ネーションズ$ ^リーグ/*リーグ$ ^（/（<lpar>$ ^Volleyball/*Volleyball$ ^Nations/*Nations$ ^League/*League$ ^）/）<rpar>$ ^は/*は$ ^、/、<cm>$ ^FIVB/*FIVB$ ^（/（<lpar>$ ^国際/*国際$ ^バレーボール/*バレーボール$ ^連盟/*連盟$ ^）/）<rpar>$ ^が/*が$ ^2018/2018<num><abs>$ ^年/*年$ ^から/*から$ ^開催/*開催$ ^し/*し$ ^て/*て$ ^いる/*いる$ ^バレーボール/*バレーボール$ ^国際/*国際$ ^大会/*大会$ ^で/*で$ ^ある/*ある$ ^。/。<sent>$ ^男子/*男子$ ^の/*の$ ^バレーボール/*バレーボール$ ^・/*・$ ^ワールド/*ワールド$ ^リーグ/*リーグ$ ^と/*と$ ^女子/*女子$ ^の/*の$ ^バレーボール/*バレーボール$ ^・/*・$ ^ワールド/*ワールド$ ^グランプリ/*グランプリ$ ^を/*を$ ^発展/*発展$ ^的/*的$ ^に/*に$ ^統合/*統合$ ^し/*し$ ^た/*た$ ^大会/*大会$ ^と/*と$ ^なる/*なる$

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

Brief summary of Sentencepiece:'SentencePiece' solves problem by using 'subwords'. First, the text is split into words and the frequency of each word is determined. High frequency words are then treated as a single vocabulary, while low frequency words are split into shorter vocabulary words. The splitting is then repeated until the vocabulary number reaches a pre-specified number. This makes it possible to eliminate unknown words while keeping the vocabulary size small.


For speed comparison, I used bochan.txt, which is fairly large japanese corpus. I got initinal speed with only one japanese word. 

Below is screenshot of sentencepiece word segmentation(62%)

![Screenshot from 2023-06-22 09-03-49](https://github.com/yypy22/gsoc_try/assets/99264752/e9615d7a-4eac-4845-abaf-d12327a9a828)

Below is with 85% one
![Screenshot from 2023-06-23 00-44-55](https://github.com/yypy22/gsoc_try/assets/99264752/d5f456b4-c0f7-4001-aca7-6a3d8464b37a)
