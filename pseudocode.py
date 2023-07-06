#This Python file use MeCab for tokenisation and hfst for fst. 
#mecab-python3 is needed with ipa dictionary. More info on pypl

##import library##
Import mecab and hfst

##mecab tagger for word segmentation##
##option Owakatti is used##
mecab_tokenizer = mecab.Tagger("-Owakatti")


##tokenizer##
def tokenise(sys.in)
output = mecab_tokeniser(sys.in)
return output

##analyser##
def analyzer(sys.in, analyser)
output = mecab_tokeniser(sys.stdin)
analyze with tokenized characters(output)
return alalysis

##process_stream function##
def process_strream(tokenizer,sts.in, sys.out, analyzer)
##if just tokenise##
if analyzer is none:
  go to tokenizer
  sys.out.write(output)
  print(sys.out)
else:
  go to analyzer
  sys.out.write(output)
  print(sys.out)

## from tokenize.py main##
if __name__ == '__main__':
    import argparse
    prs = argparse.ArgumentParser(description='Segment input stream using HFST')
    prs.add_argument('transducer')
    prs.add_argument('analyzer', nargs='?')
    args = prs.parse_args()
    stream_tok = hfst.HfstInputStream(args.transducer)
    tokenizer = hfst.HfstBasicTransducer(stream_tok.read())
    analyzer = None
    if args.analyzer:
        stream_morf = hfst.HfstInputStream(args.analyzer)
        analyzer = hfst.HfstBasicTransducer(stream_morf.read())
    import sys
    process_stream(tokenizer, sys.stdin, sys.stdout, analyzer)

