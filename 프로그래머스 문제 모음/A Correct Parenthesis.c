#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

typedef struct ListNode{
    char c;
    struct Node* next;
}Stack;

bool isEmptyStack(Stack* top){
    return (top == NULL);
}

void push(Stack** top, char c, int* size){
        
    Stack* new_node = (Stack*)malloc(sizeof(Stack));
    
    if(new_node == NULL){
        //printf("stack is full!!\n");
        return;
    }
    
    new_node->c = c;
    new_node->next = *top;
    
    *top = new_node;
    (*size)++;
    //printf("%c is pushed to stack\n", new_node->c);
}

char pop(char** top, int* size){
    
    if(isEmptyStack(*top)){
        //printf("stack is empty\n");
        return NULL;
    }else{
        Stack* temp = NULL;
        temp = *top;
        char data = temp->c;
        *top = temp->next;
        free(temp);
        (*size)--;
        return data;
    }
}




// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
bool solution(const char* s) {
    bool answer = true;
    Stack* stack = NULL;
    int stack_size = 0;
    
    // push(&stack, 'a', &stack_size);
    // printf("size : %d\n", stack_size);
    // push(&stack, 'b', &stack_size);
    // printf("size : %d\n", stack_size);
    // push(&stack, 'c', &stack_size);
    // printf("size : %d\n", stack_size);
    // printf("%c is poped\n", pop(&stack, &stack_size));
    // printf("size : %d\n", stack_size);
    // printf("%c is poped\n", pop(&stack, &stack_size));
    // printf("size : %d\n", stack_size);
    // printf("%c is poped\n", pop(&stack, &stack_size));
    // printf("size : %d\n", stack_size);
    
    int str_len = strlen(s);
    
    for(int i=0; i < str_len; i++){
        char current_char = s[i];
        
        if((stack_size > 0) && (current_char == ')') && (stack->c == '(')){
            pop(&stack, &stack_size);
        }else{
            push(&stack, current_char, &stack_size);
        }
    }
    
    
    if(stack_size > 0){
        return false;
    }else{
        return true;
    }
}