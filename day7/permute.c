#include <stdio.h>
#define exchange(x,y,t) ((t) = (x), (x) = (y), (y) = (t))
// x는 y로, y는 x로
void word(char*, int, int);

int start = 0, end = 3;

void main(){
    char letter[] = {'S', 'M', 'W', 'U', 'T'};
    scanf("%d", &start);
    scanf("%d", &end);
    word(letter, start, end);
}

void word(char *letter, int i, int n){
    int j, temp;
    if (i==n){
        for (j=start;j<=n;j++){
            printf("%c", letter[j]);
        }
        printf("\n");
    }
    else {
    for (j=i;j<=n;j++){
        exchange(letter[i], letter[j], temp);
        word(letter, i+1, n);
        exchange(letter[i], letter[j], temp);
    }}
}