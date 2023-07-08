#include <iostream>
#include <mecab.h>

int main(int argc, char **argv) {

    char input[1024] = "ただ、冒頭のリンク先の問題では通りましたが、";
    MeCab::Tagger *tagger = MeCab::createTagger("-Owakati");
    const char *result = tagger->parse(input);
    std::cout << result << std::endl;

    delete tagger;
    return 0;
}
