; nasm -felf64 aoc2016_16_part2_nogolf.asm -oa.o && ld a.o && ./a.out

section .rodata
init: db "10010000000110000",0
N   equ 35651584

section .bss
buf:    resb N*2+1

section .text
    global _start
_start:

    ; copy initializer
    xor rcx, rcx        ; zero bytes copied so far
    mov rsi, init       ; set source and destination
    mov rdi, buf
copyinit:
    inc rcx             ; count byte
    lodsb               ; copy byte (no movs because we need to examine it)
    stosb
    or al, al           ; exit on terminator
    jnz copyinit
    dec rcx             ; copied one byte too many

    ; expansion step
expand:
    cmp rcx, N
    jae endexpand       ; check if done and exit
    lea rsi, [buf+rcx]
    mov rdi, rsi        ; point rsi and rdi to end of buffer ...
    mov al, 48          ; ... and put a '0' there
    stosb
    mov rbx, rcx        ; set loop counter
expandloop:
    dec rsi             ; load a byte
    mov al, [rsi]
    xor al, 1           ; modify and store it
    stosb
    dec rbx             ; decrease loop counter and branch
    jnz expandloop
    lea rcx, [rcx*2+1]  ; set new length
    jmp expand
endexpand:
    mov rcx, N          ; truncate to indicated length

    ; reduction step
reduce:
    test rcx, 1         ; odd/even check
    jnz endreduce
    mov rsi, buf        ; set buffer pointers
    mov rdi, buf
    shr rcx, 1          ; half the size and load the counter
    mov rbx, rcx
reduceloop:
    lodsb               ; load-modify-store cycle
    mov ah, al
    lodsb
    xor al, ah
    xor al, 49
    stosb
    dec rbx             ; decrease loop counter and branch
    jnz reduceloop
    jmp reduce
endreduce:

    ; terminate the string with a newline and write() it
    mov byte [buf+rcx], 10
    mov rax, 1          ; rax = syscall number
    mov rdi, rax        ; rdi = fd (1 = stdout)
    mov rsi, buf        ; rsi = buffer
    lea rdx, [rcx+1]    ; rdx = size
    syscall

    ; exit()
    mov rax, 60         ; rax = syscall number
    xor rdi, rdi        ; rdi = exit code
    syscall
