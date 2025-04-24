section .text
    global convertir_y_sumar_asm

convertir_y_sumar_asm:
    ; Redondear el valor float en xmm0 al entero más cercano
    roundss xmm0, xmm0, 0b00000000     ; modo 0: round to nearest

    ; Convertir el valor ya redondeado a entero
    cvttss2si rax, xmm0

    ; Sumar 1
    add rax, 1

    ret
   