#include<stdio.h>
#include<conio.h>
#include <time.h>

int main(){
    clock_t start, end;
    double cpu_time_used;
     
    start = clock();
    int res=0;

    for(int i=0; i<20000; i++){
        for(int j=1; j<20000; j++){
            res = res + j;
            // printf("%d", res);
        }
    }

    printf("%d",res);
    printf("\n");
    end = clock();
    cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
    printf("%lf", cpu_time_used);

}