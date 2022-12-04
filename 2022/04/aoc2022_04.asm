; yasm -fbin -oaoc22_04.com aoc2022_04.asm && dosbox aoc22_04.com
; yasm -fbin -oaoc22_04.com aoc2022_04.asm && dosbox -c "mount c: $HOME/Downloads" -c "mount d: ." -c "d:" -c "c:td aoc22_04.com"

BITS 16
CPU  8086
ORG  100h

; local variables; these will overwrite the initial part of the code
bss     EQU $
numbers EQU bss         ; the four numbers on each line
bss_end EQU numbers + 1 ; end of BSS section

    ; open file
    mov ax, 3D00h       ; DOS function "open file" (for reading)
    mov dx, file
    int 21h
    jc io_err
    mov bx, ax          ; save file handle for next operation

    ; read file contents into the (nearly) 64k of empty space in this .COM file
    mov ah, 3Fh         ; DOS function "read file"
    mov cx, 0FF00h      ; read as much as we (somewhat) safely can
    sub cx, dx
    int 21h
    jnc io_ok
io_err:
    mov ax, 4C01h       ; DOS function "terminate program" (with exit code 1)
    int 21h
io_ok:
    mov si, dx          ; store address of 'file' variable for later
    add dx, ax          ; append null terminator to end of file data
    mov di, dx
    xor ax, ax
    stosb

    ; close file (optional - the OS will clean up our mess too, if needed :)
;    mov ah, 3Eh         ; DOS function "close file"
;    int 21h

    ; iterate over the input file
nextline:
    mov bl, 10          ; common multiplier for numbers
    mov di, numbers     ; reset number pointer
nextnum:
    xor dx, dx          ; reset current number accumulator
nextbyte:
    lodsb               ; load a byte
    or al, al           ; terminator byte? -> EOF
    jz eof
    sub al, '0'         ; convert ASCII to number
    cmp al, 9           ; is is a valid digit?
    ja nodigit
    xchg ax, dx         ; swap number accumulator and current digit
    mul bl              ; multiply accumulator by 10
    add dl, al          ; ... and add current digit
    jmp nextbyte
nodigit:
    or dx, dx           ; not a valid digit -> flush current number (if not zero)
    jz .dxzero
    xchg ax, dx         ; current number is valid -> store it
    stosb
    xchg ax, dx         ; restore value
.dxzero:
    cmp al, 0Ah - '0'   ; end of line?
    je eol
    jmp nextnum

eol:
    ; end of line -> load intervals into AL-AH, BL-BH
    mov ax, [numbers]
    mov bx, [numbers+2]

    ; part 1 evaluation: ((AL >= BL) and (AH <= BH)) or ((BL >= AL) and (BH <= AH))
    cmp al, bl
    jb .p1b
    cmp ah, bh
    jbe .p1hit
.p1b:
    cmp bl, al
    jb .p1miss
    cmp bh, ah
    ja .p1miss
.p1hit:
    inc word [part1]
.p1miss:

    ; part 2 evaluation: (BL <= AH) and (AL <= BH)
    cmp bl, ah
    ja .p2miss
    cmp al, bh
    ja .p2miss
.p2hit:
    inc word [part2]
.p2miss:

    jmp nextline

eof:
    mov ax, [part1]
    call OutputWord
    mov ax, [part2]
    ; now run right into the OutputWord function which will also exit the program

; -----------------------------------------------------------------------------
; FUNCTION: OutputWord - output a word in decimal onto the screen
; in AX = word to output
; clobbers BX, CX, DX
OutputWord:
    ; add terminating EOL to output stack
    mov bl, 0Ah
    push bx
    mov bl, 0Dh
    push bx

.nextdigit:
    mov bx, 10          ; common quotient
    xor dx, dx          ; clear upper part
    div bx              ; divide
    add dl, '0'         ; convert remainder into ASCII
    push dx             ; ... and store to output stack
    or ax, ax           ; another iteration if value is still nonzero
    jnz .nextdigit

    ; flush output stack
    mov ah, 2           ; DOS function "write character"
.outchar:
    pop dx
    int 21h
    cmp dl, 0Ah
    jne .outchar

    ret

; -----------------------------------------------------------------------------
; DATA SECTION

; result scores
part1 dw 0
part2 dw 0

; input filename; gets overwritten with file data later
file: db "INPUT.TXT", 0
