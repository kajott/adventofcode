; yasm -fbin -oaoc22_02.com aoc2022_02.asm && dosbox aoc22_02.com
; yasm -fbin -oaoc22_02.com aoc2022_02.asm && dosbox -c "mount c: ." -c "c:" -c "td aoc22_02.com"

BITS 16
CPU  8086
ORG  100h

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

    ; now iterate over the input file
nextchar:
    lodsb               ; load a byte
    or al, al           ; EOF reached?
    jz eof
    cmp al, 'C'         ; is is possibly an XYZ value?
    ja .maybe_xyz
    sub al, 'A'         ; not XYZ -> check for ABC (and map to ABC=012)
    cmp al, 3
    jae nextchar        ; not a valid character
    inc al              ; save decoded ABC value (mapped to ABC=123)
    mov ah, al
    jmp nextchar
.maybe_xyz:
    sub al, 'X'         ; check for XYZ (and map to XYZ=012)
    cmp al, 3
    jae nextchar        ; not a valid character
    push ax             ; save original result (will be clobbered in part 1 evaluation)

    ; part 1: check if we have won
    xor cx, cx          ; reset score
    inc al              ; remap our result to XYZ=123
    cmp ah, al          ; draw?
    je .p1_draw
    inc ah              ; correct_guess = opponents_guess + 1
    cmp ah, 4           ; ... with wrap-around
    jb .p1_nowrap
    sub ah, 3
.p1_nowrap:
    cmp ah, al          ; won?
    jne .p1_finish      ; if not, just add score
    add cl, 3           ; add 3 (of 6) points for win
.p1_draw:
    add cl, 3           ; add 3 points for draw (or another 3 points for win)
.p1_finish:
    add cl, al          ; add score for local player's choice
    add [part1], cx     ; add to accumulator

    ; part 2: create a suitable score
    pop ax              ; restore the original input data
    xor cx, cx          ; reset score
    add cl, al          ; ... and set to 3 * winning_indicator
    add cl, al
    add cl, al
    add al, 2           ; convert winning_indicator to offset: lose=2, draw=3(=0 mod 3), win=4(=1 mod 3)
    add al, ah          ; ... and add offset to opponent's choice to get our choice
.p2_wrapcheck:
    cmp al, 4           ; check for wrap-around
    jb .p2_nowrap
    sub al, 3
    jmp .p2_wrapcheck
.p2_nowrap:
    add cl, al          ; add score for local player's choice
    add [part2], cx     ; add to accumulator

    jmp nextchar        ; continue with next input character

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

; score accumulators for parts 1 and 2
part1 dw 0
part2 dw 0

; input filename; gets overwritten with file data later
file: db "INPUT.TXT", 0
