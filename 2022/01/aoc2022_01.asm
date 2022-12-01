; yasm -fbin -oaoc22_01.com aoc2022_01.asm && dosbox aoc22_01.com
; yasm -fbin -oaoc22_01.com aoc2022_01.asm && dosbox -c "mount c: ." -c "c:" -c "td aoc22_01.com"

BITS 16
CPU  8086
ORG  100h

; local variables; these will overwrite the initial part of the code
bss     EQU $
cga_lo  EQU bss          ; current group accumulator (CGA)
cga_hi  EQU cga_lo  + 2
max3_lo EQU cga_hi  + 2  ; third maximum
max3_hi EQU max3_lo + 2
max2_lo EQU max3_hi + 2  ; second maximum
max2_hi EQU max2_lo + 2
max1_lo EQU max2_hi + 2  ; first (= real) maximum
max1_hi EQU max1_lo + 2
bss_end EQU max1_hi + 2  ; end of BSS section

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
    mov byte [di], 0

    ; close file (optional - the OS will clean up our mess too, if needed :)
;    mov ah, 3Eh         ; DOS function "close file"
;    int 21h

    ; clear variable space
    mov di, bss
    mov cx, (bss_end - bss) / 2
    xor ax, ax
    rep stosw

    ; iterate over the input file
nextnumber:
    mov bx, 10          ; general base for multiplications
    xor cx, cx          ; reset current number accumulator (CNA) in DX:CX
    xor dx, dx
nextchar:
    lodsb               ; load and inspect next character
    or al, al           ; (*) null byte -> end of file
    jz input_done
    cmp al, 0Ah         ; (*) LF -> end of line
    je eol
    sub al, '0'         ; convert from ASCII to digit
    cmp al, 9           ; (*) not a valid ASCII digit -> ignore
    ja nextchar

    ; new digit read -> add to CNA
    xor ah, ah          ; remove garbage from upper byte
    push ax             ; save current digit
    ; first multiply CNA by 10
    push dx             ; save upper part
    mov ax, cx          ; lower part multiply
    mul bx
    mov cx, ax
    mov di, dx          ; save overflow from lower part
    pop ax              ; load upper part and multiply
    mul bx
    mov dx, ax
    ; then add current digit
    pop ax              ; load current digit
    add cx, ax          ; add to lower part
    adc dx, di          ; add carry and overflow from lower multiplication
    jmp nextchar        ; continue input parsing

eol:
    ; end of line
    mov ax, cx          ; do we have a current number?
    or ax, dx
    jz eog              ; if not, this line is empty -> end of group
    add [cga_lo], cx    ; otherwise, add to CGA
    adc [cga_hi], dx
    xor cx, cx          ; clear CNA
    xor dx, dx
    jmp nextchar        ; continue input parsing

eog:
    ; end of group -> finish it and prepare the next one
    call FinishGroup    ; sort the CGA appropriately
    xor ax, ax          ; clear CGA for next group
    mov [cga_lo], ax
    mov [cga_hi], ax
    jmp nextnumber      ; continue input parsing (but reset CNA first)

input_done:
    call FinishGroup    ; don't forget the last group!

    ; part 1 solution: just output the maximum value
    mov ax, [max1_lo]   ; load the maximum value
    mov dx, [max1_hi]
    push dx             ; save it, we'll need it again
    push ax
    call OutputDWord
    pop ax
    pop dx

    ; part 2 solution: sum the other two maxima
    add ax, [max3_lo]
    adc dx, [max3_hi]
    add ax, [max2_lo]
    adc dx, [max2_hi]
    ; now run right into the OutputDWord function which will also exit the program

; -----------------------------------------------------------------------------
; FUNCTION: OutputDWord - output a doubleword in decimal onto the screen
; in DX:AX = dword to output
; clobbers BX, CX
OutputDWord:
    ; add terminating EOL to output stack
    mov bl, 0Ah
    push bx
    mov bl, 0Dh
    push bx

.nextdigit:
    mov bx, 10          ; common quotient
    mov cx, ax          ; save lower part
    mov ax, dx          ; rotate upper part into lower
    xor dx, dx
    div bx              ; divide upper part
    xchg cx, ax         ; save upper part result, restore lower part
    div bx              ; divide lower part
    add dl, '0'         ; convert remainder into ASCII
    push dx             ; ... and store to output stack
    mov dx, cx          ; reload upper part
    or cx, ax           ; another iteration if either part is nonzero
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
; FUNCTION: FinishGroup - perform ripple-sort at the end of a group
FinishGroup:
    mov bx, cga_lo      ; load base address of words to sort
    mov cx, 3           ; loop max. 3 times
.sort_loop:
    mov ax, [bx+2]      ; compare high words
    cmp ax, [bx+6]
    jb .sort_done       ; hi(curr) < hi(next) => curr < next => end of sort
    ja .sort_swap       ; hi(curr) > hi(next) => curr > next => swap and continue
    mov ax, [bx]        ; compare low words
    cmp ax, [bx+4]
    jbe .sort_cont      ; curr <= next => continue [else: swap first]
.sort_swap:    
    mov ax, [bx+4]      ; load next from memory
    mov dx, [bx+6]
    xchg ax, [bx]       ; swap current with loaded next
    xchg dx, [bx+2]
    mov [bx+4], ax      ; save swapped values
    mov [bx+6], dx
.sort_cont:
    add bx, 4
    loop .sort_loop
.sort_done:
    ret

; -----------------------------------------------------------------------------
; DATA SECTION

; input filename; gets overwritten with file data later
file: db "INPUT.TXT", 0
