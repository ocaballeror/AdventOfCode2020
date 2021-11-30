#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

#define BOOL short int
#define TRUE 1
#define FALSE 0

char* read_input() {
    FILE *fp = fopen("input", "r");
    if(!fp) {
        perror("Cannot read input");
        exit(1);
    }

    fseek(fp, 0, SEEK_END);
    size_t fsize = ftell(fp);
    fseek(fp, 0, SEEK_SET);

    char *content = malloc(fsize * sizeof(char));
    fread(content, 1, fsize, fp);
    fclose(fp);

    return content;
}

long evaluate(char**, BOOL);

/**
 * Read one operand, which could be a flat number or a parenthesized expression.
 *
 * If it's the latter, compute the expression contained inside and return its value.
 */
long read_operand(char** expr, BOOL prio_sum) {
    char read = **expr;
    long operand;
    if(read == '(') {
        (*expr)++;
        operand = evaluate(expr, prio_sum);
    } else {
        operand = read - 48;  // convert char to int
    }
    return operand;
}

/**
 * Evaluate a single expression string
 * */
long evaluate(char** expr, BOOL prio_sum) {
    // store mult operations in an array and compute them at the end
    int* multbuffer = malloc(strlen(*expr));
    int multbuffer_len = 0;

    long left = 0, right = -1;
    char op = 0;
    for(char read = **expr; **expr!=0; (*expr)++) {
        read = **expr;
        if(read == ' ') continue;
        if(read == '\n'){
            // end of the expression. consume \n and return
            (*expr)++;
            break;
        }

        if(left == 0) {
            left = read_operand(expr, prio_sum);
            /* printf("Assign left to %ld\n", left); */
        } else if(op == 0) {
            op = read;
            /* printf("Assign op to %c\n", op); */
            if(op == '*' && prio_sum) {
                // append multiplication operation to the buffer for later processing
                multbuffer[multbuffer_len] = left;
                multbuffer_len++;
                /* printf("Append *%ld to multbuffer\n", left); */
                op = 0;
                left = 0;
            } else if(op == ')') {
                // end of the subexpression. calculate result and return
                break;
            }
        } else if(right == -1) {
            right = read_operand(expr, prio_sum);
            /* printf("Assign right to %ld\n", right); */

            // calculate sum operations right away
            if(op == '+') {
                left += right;
            } else if (!prio_sum && op == '*') {
                left *= right;
            }
            op = 0;
            right = -1;
        }
    }

    // process all the pending mult operations
    for(int i = 0; i < multbuffer_len; i++) {
        left *= multbuffer[i];
    }

    /* printf("%sResult: %ld\n", op == ')'? "(sub) ":"", left); */
    free(multbuffer);
    return left;
}

/**
 * Evaluate each line of the given string as a separate expression and add up all the results
 *
 * Args:
 *     input: The full string with \n separated expressions
 *     prio_sum: Whether to prioritize sums over multiplications
 * */
long eval_lines(char* input, BOOL prio_sum) {
    char* cursor = input;
    long sum = 0;
    while(*cursor != 0) {
        sum += evaluate(&cursor, prio_sum);
    }

    return sum;
}

int main() {
    char* input = read_input();
    long part1 = eval_lines(input, FALSE);
    printf("Part 1: %ld\n", part1);
    long part2 = eval_lines(input, TRUE);
    printf("Part 2: %ld\n", part2);
    free(input);

    return 0;
}
