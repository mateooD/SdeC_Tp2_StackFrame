section .text
    global convertir_y_sumar_asm   ; Hacemos pública la función

convertir_y_sumar_asm:
    ; Recibimos un número float en xmm0 (pasado desde C)
    ; Convertimos de float a entero truncado y le sumamos 1
    cvttss2si rax, xmm0         ; Convertir de float a entero (en rax)
    add     rax, 1              ; Sumar 1 al valor entero
    ret                         ; Devolver el resultado (en rax)
 

   