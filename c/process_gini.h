#ifndef PROCESS_GINI_H
#define PROCESS_GINI_H
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/*
    Esta funcion transforma de tipo float a tipo int y le suma 1 
    a cada elemento de la array proveniente del codigo en python 
    @param arr :arreglo con los indices gini
    @param size :tamaño del arreglo
*/
int* convertir_y_sumar(float *arr, int size);

#endif
