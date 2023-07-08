#include <iostream>
#include <string>
#include <vector>
#include <mecab.h>

void go_to_tokenize(std::istream& sin, std::ostream& sout) {
    std::string input;
    std::getline(sin, input);

    std::vector<std::string> excluded;
    std::string current;
    bool in_blank = false;

    for (char i : input) {
        if (i == '[') {
            current = "";
            in_blank = true;
        } else if (i == ']') {
            current += i;
            in_blank = false;
            excluded.push_back(current);
            current = "";
        }
        if (in_blank) {
            current += i;
        }
    }

    std::string tokenized_input;
    size_t placeholder = 0;

    for (const std::string& token : excluded) {
        size_t pos = input.find(token);
        while (pos != std::string::npos) {
            input.replace(pos, token.length(), "^" + std::to_string(placeholder) + "^");
            pos = input.find(token, pos + 1);
        }
        ++placeholder;
    }

    MeCab::Tagger* tagger = MeCab::createTagger("-Owakati");
    const char* result = tagger->parse(input.c_str());

    std::string tokenized(result);
    placeholder = 0;

    for (const std::string& excluded_token : excluded) {
        std::string replaceStr = "^ " + std::to_string(placeholder) + " ^";
        size_t pos = 0;
        while ((pos = tokenized.find(replaceStr, pos)) != std::string::npos) {
            tokenized.replace(pos, replaceStr.length(), excluded_token);
            pos += excluded_token.length();
        }
        ++placeholder;
    }

    sout << tokenized;

    delete tagger;
}

int main() {
    go_to_tokenize(std::cin, std::cout);
    return 0;
}
