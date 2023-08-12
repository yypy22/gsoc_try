#include <iostream>
#include <fstream>
#include <string>
#include <mecab.h>

void process_text(std::istream& sin, std::ostream& sout) {
    std::string text((std::istreambuf_iterator<char>(sin)),
                     std::istreambuf_iterator<char>());

    MeCab::Tagger *mecab = MeCab::createTagger("-Owakati");
    std::string buffer;
    std::string tokenized;
    bool in_bracket = false;

    for (char char : text) {
        if (char == '[') {
            if (!buffer.empty()) {
                const char *parsed = mecab->parse(buffer.c_str());
                tokenized += std::string(parsed).substr(0, std::strlen(parsed) - 1) + ' ';
            }
            tokenized += '[';
            buffer.clear();
            in_bracket = true;
        } else if (char == ']') {
            if (in_bracket) {
                const char *parsed = mecab->parse(buffer.c_str());
                std::string stripped(parsed);
                stripped.erase(std::remove(stripped.begin(), stripped.end(), '\n'), stripped.end());
                tokenized += stripped + ']';
                buffer.clear();
            }
            in_bracket = false;
        } else {
            buffer += char;
        }
    }

    if (!buffer.empty()) {
        const char *parsed = mecab->parse(buffer.c_str());
        tokenized += std::string(parsed).substr(0, std::strlen(parsed) - 1);
    }

    sout << tokenized;
    delete mecab;
}

int main() {
    process_text(std::cin, std::cout);
    return 0;
}
