#include <stdio.h>

// Declaración de la función de assembler
int convertir_y_sumar(float valor);

int main() {
    float valor = 42.5;
    int resultado = convertir_y_sumar(valor);
    printf("Valor original: %.2f\n", valor);
    printf("Resultado de convertir_y_sumar: %d\n", resultado);
    return 0;
}
