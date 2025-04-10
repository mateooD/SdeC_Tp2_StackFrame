#include "process_gini.h"

int* convertir_y_sumar(float *arr, int size) {
    int* array_int = malloc(size * sizeof(int));
    for(int i=0;i<size;i++){
        array_int[i]=(int)arr[i];
        array_int[i]++;
    }
    return array_int;
}
void free_memory(int *arr){
    free(arr);
}
