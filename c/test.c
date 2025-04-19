
#include <stdio.h>

// Declaración de la función de assembler
 

int convertir_y_sumar_asm(float valor);


int main() {
 

    float valor = 42.7;
 

    int resultado = convertir_y_sumar_asm(valor);

    printf("Valor original: %.2f\n", valor);
 

    printf("Resultado de convertir_y_sumar: %d\n", resultado);
 

    return 0;


}