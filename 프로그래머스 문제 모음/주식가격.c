#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

typedef struct Data{
    int price;
    int index;
}Data;

typedef struct ListNode{
    Data data;
    struct ListNode* next;
}Stack;

bool isStackEmpty(Stack* top){
    return (top == NULL);
}


void push(Stack** top, int price, int index, int* stack_size){
    
    Stack* new_node = (Stack*)malloc(sizeof(Stack));
    
    new_node->data.price = price;
    new_node->data.index = index;
    new_node->next = *top;
    (*stack_size)++;
    
    *top = new_node;
}

Data pop(Stack** top, int* stack_size){
    
    Stack* temp = NULL;
    
    temp = *top;
    
    Data poped_data;
    poped_data.price = temp->data.price;
    poped_data.index = temp->data.index;
    *top = temp->next;
    (*stack_size)--;
    free(temp);
    return poped_data;  
}



// prices_len은 배열 prices의 길이입니다.
int* solution(int prices[], size_t prices_len) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int* answer = (int*)malloc(sizeof(int)*prices_len);
    Stack* top = NULL;
    int stack_size = 0;
    
    for(int i = 0; i < prices_len; i++){
        answer[i] = (prices_len-1)-i;
    }
    
    for(int i = 0; i < prices_len; i++){
        int cur_price = prices[i];
        int index = i;
        
        while((stack_size > 0) && (top->data.price > cur_price)){
            Data data = pop(&top, &stack_size);
            answer[data.index] = i - data.index;
        }
        
        push(&top, cur_price, index, &stack_size);
    }
    
    return answer;
}