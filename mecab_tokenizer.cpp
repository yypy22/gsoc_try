#include <iostream>
#include <mecab.h>
#include <string>

int main() {
    //simple tokenization with user input
    std::string input;
    
    MeCab::Tagger *tagger = MeCab::createTagger("-Owakati");

    std::cout << "Enter your input: ";
    std::getline(std::cin, input);

    const char *result = tagger->parse(input.c_str());
    std::cout << result << std::endl;

    delete tagger;
    return 0;
}
