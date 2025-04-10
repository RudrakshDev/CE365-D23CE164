#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

#define MAX_TOKENS 100
#define MAX_SYMBOLS 100
#define MAX_LEXEME_LENGTH 100

typedef struct {
    char name[MAX_LEXEME_LENGTH];
} SymbolTable;

SymbolTable symbolTable[MAX_SYMBOLS];
int symbolTableCount = 0;

const char *keywords[] = {
    "int", "char", "return", "void", "long", "float", "double", "struct", "if", "else", "for", "while", "do", "switch",
    "case", "break", "continue", "default", "const", "unsigned", "typedef", "sizeof", "static"
};
const int keywordCount = sizeof(keywords) / sizeof(keywords[0]);

const char operators[] = "+-*/%=<>&|^!";
const char punctuations[] = "(),{}[];";

int isKeyword(const char *lexeme) {
    for (int i = 0; i < keywordCount; i++) {
        if (strcmp(lexeme, keywords[i]) == 0) {
            return 1;
        }
    }
    return 0;
}

void addToSymbolTable(const char *identifier) {
    for (int i = 0; i < symbolTableCount; i++) {
        if (strcmp(symbolTable[i].name, identifier) == 0) {
            return;
        }
    }
    strcpy(symbolTable[symbolTableCount++].name, identifier);
}

void lexicalAnalyzer(FILE *file) {
    char c, buffer[MAX_LEXEME_LENGTH];
    int i = 0;
    int line = 1;

    printf("TOKENS:\n");
    while ((c = fgetc(file)) != EOF) {
        if (c == '\n') {
            line++;
        }

        if (isspace(c)) {
            continue;
        }

        if (c == '/' && (c = fgetc(file)) == '/') {
            while ((c = fgetc(file)) != '\n' && c != EOF) {}
            line++;
            continue;
        }

        if (c == '/' && (c = fgetc(file)) == '*') {
            while ((c = fgetc(file)) != EOF) {
                if (c == '*' && (c = fgetc(file)) == '/') {
                    break;
                }
                if (c == '\n') {
                    line++;
                }
            }
            continue;
        }

        if (isalpha(c) || c == '_') {
            buffer[i++] = c;
            while (isalnum((c = fgetc(file))) || c == '_') {
                buffer[i++] = c;
            }
            buffer[i] = '\0';
            i = 0;

            if (isKeyword(buffer)) {
                printf("Keyword: %s\n", buffer);
            } else {
                printf("Identifier: %s\n", buffer);
                addToSymbolTable(buffer);
            }
            ungetc(c, file); 
        }

        else if (isdigit(c)) {
            buffer[i++] = c;
            while (isdigit((c = fgetc(file)))) {
                buffer[i++] = c;
            }
            buffer[i] = '\0';
            i = 0;

            if (isalpha(c)) { 
                printf("LEXICAL ERROR: %s at line %d\n", buffer, line);
                while (isalnum(c)) {
                    c = fgetc(file);
                }
            } else {
                printf("Constant: %s\n", buffer);
            }
            ungetc(c, file);
        }

        else if (c == '\"' || c == '\'') {
            char quoteType = c;
            buffer[i++] = c;
            while ((c = fgetc(file)) != EOF && c != quoteType) {
                buffer[i++] = c;
            }
            buffer[i++] = quoteType;
            buffer[i] = '\0';
            i = 0;

            printf("String: %s\n", buffer);
        }

        else if (strchr(operators, c)) {
            printf("Operator: %c\n", c);
        }

        else if (strchr(punctuations, c)) {
            printf("Punctuation: %c\n", c);
        }

        else {
            printf("LEXICAL ERROR: Unknown character '%c' at line %d\n", c, line);
        }
    }

    printf("\nSYMBOL TABLE ENTRIES:\n");
    for (int i = 0; i < symbolTableCount; i++) {
        printf("%d) %s\n", i + 1, symbolTable[i].name);
    }
}

int main() {
    char filename[100];
    FILE *file;

    printf("Enter the name of the C source file: ");
    scanf("%s", filename);

    file = fopen(filename, "r");
    if (file == NULL) {
        printf("Error: Unable to open file %s\n", filename);
        return 1;
    }

    lexicalAnalyzer(file);

    fclose(file);
    return 0;
}
