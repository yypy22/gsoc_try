import MeCab 
import hfst
from itertools import product

mecab_tokenizer = MeCab.Tagger("-Owakati")

def tokenizer_mecab(sin, sout):
    if sin is None:
        return ""
    else:
        sout.write(mecab_tokenizer.parse(sin))
        return sout

def analyzer_mecab(sin, sout):
    if sin is None:
        return ""
    else:
        lines = ""
        sout.write(mecab_tokenizer.parse(sin))
        # for i in range(len(sout)):
        #     lines += (sout[i] + "^")
        return lines

def process_stream(tokenizer, sin, sout, analyzer=None):
    alpha = tokenizer.get_alphabet()
    cur_word = ''
    while True:
        c = sin.read(1)
        if c in alpha:
            cur_word += c
        else:
            if cur_word:
                if analyzer:
                    analyzer_mecab(cur_word, sout)
                else:
                    tokenizer_mecab(cur_word, sout)
            if c:
                cur_word = ''
                sout.write(c)
            else:
                break

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
