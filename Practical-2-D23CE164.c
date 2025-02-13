#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_STATES 100
#define MAX_SYMBOLS 26

int validateString(int numStates, int numSymbols, char symbols[], int startState, int acceptStates[], int numAcceptStates, int transitionTable[MAX_STATES][MAX_SYMBOLS], char *inputString) {
    int currentState = startState;
    for (int i = 0; i < strlen(inputString); i++) {
        char currentSymbol = inputString[i];
        
        int symbolIndex = -1;
        for (int j = 0; j < numSymbols; j++) {
            if (symbols[j] == currentSymbol) {
                symbolIndex = j;
                break;
            }
        }
        
        if (symbolIndex == -1) {
            return 0; 
        }
        
        currentState = transitionTable[currentState][symbolIndex];
        
        if (currentState == -1) {
            return 0;
        }
    }
    
    for (int i = 0; i < numAcceptStates; i++) {
        if (currentState == acceptStates[i]) {
            return 1; 
        }
    }
    return 0;
}

int main() {
    int numSymbols, numStates, startState, numAcceptStates;
    char symbols[MAX_SYMBOLS];
    int acceptStates[MAX_STATES];
    int transitionTable[MAX_STATES][MAX_SYMBOLS];
    
    printf("Number of input symbols: ");
    scanf("%d", &numSymbols);
    printf("Input symbols (space-separated): ");
    for (int i = 0; i < numSymbols; i++) {
        scanf(" %c", &symbols[i]);
    }
    
    printf("Enter number of states: ");
    scanf("%d", &numStates);
    printf("Initial state: ");
    scanf("%d", &startState);
    
    printf("Number of accepting states: ");
    scanf("%d", &numAcceptStates);
    printf("Accepting states (space-separated): ");
    for (int i = 0; i < numAcceptStates; i++) {
        scanf("%d", &acceptStates[i]);
    }
    
    printf("Transition table:\n");
    for (int i = 1; i <= numStates; i++) {
        for (int j = 0; j < numSymbols; j++) {
            printf("State %d to %c -> ", i, symbols[j]);
            scanf("%d", &transitionTable[i][j]);
        }
    }
    
    char inputString[100];
    printf("Input string: ");
    scanf("%s", inputString);
    
    if (validateString(numStates, numSymbols, symbols, startState, acceptStates, numAcceptStates, transitionTable, inputString)) {
        printf("Valid String\n");
    } else {
        printf("Invalid String\n");
    }
    
    return 0;
}
