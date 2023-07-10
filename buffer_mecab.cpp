#include <iostream>
#include <string>
#include <sstream>
#include <mecab.h>

void process_text(std::istream& sin, std::ostream& sout) {
    //input from command
    std::string text;
    std::getline(sin, text);
    //creater tagger
    MeCab::Tagger* tagger = MeCab::createTagger("-Owakati");
    //two strings
    std::stringstream buffer;
    //std::ostringstream buffer;
    std::string tokenized;
    bool in_bracket = false;
    for (char i : text) {
        buffer << i;
        if (i == '[') {
            //i tried buffer = tagger->parse(//same) but did not work so used diff string 
            std::string parsed = tagger->parse(buffer.str().c_str());
            parsed.erase(parsed.find_last_not_of(" \n\r\t") + 1);
            tokenized += parsed;
            // buffer = tagger->parse(buffer.str().c_str());
            // tokenized += buffer;
            buffer.str("");
            buffer.clear();
            in_bracket = true;
        }
        else if (in_bracket) {
            tokenized += i;
        }
        else if (i == ']') {
            in_bracket = false;
        }
    }
    
    sout << tokenized;
    
    delete tagger;
}

int main() {
    process_text(std::cin, std::cout);
    return 0;
}
