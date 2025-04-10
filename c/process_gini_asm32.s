; process_gini_asm_32.s
section .text
    global convertir_y_sumar_asm


convertir_y_sumar_asm:
    push ebp
    mov ebp, esp

    fld dword [ebp+8]       ; cargar float en FPU
    sub esp, 4              ; espacio para guardar int
    fistp dword [esp]       ; convertir y guardar en stack
    mov eax, [esp]          ; mover a eax
    add eax, 1              ; sumar 1
    add esp, 4              ; liberar espacio

    pop ebp
    ret

