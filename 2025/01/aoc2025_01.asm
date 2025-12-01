; yasm -fbin -oaoc25_01.com aoc2025_01.asm && dosbox aoc25_01.com
; yasm -fbin -oaoc25_01.com aoc2025_01.asm && dosbox -c "mount c: $HOME/Downloads" -c "mount d: ." -c "d:" -c "c:td aoc25_01.com"

BITS 16
CPU  8086
ORG  100h

    ; open file
    mov ax, 3D00h           ; DOS function "open file" (for reading)
    mov dx, file
    int 21h
    jc io_err
    mov bx, ax              ; save file handle for next operation

    ; read file contents into the (nearly) 64k of empty space in this .COM file
    mov ah, 3Fh             ; DOS function "read file"
    mov cx, sp              ; read as much as we (somewhat) safely can without hitting the stack
    sub cx, dx
    int 21h
    jnc io_ok
io_err:
    mov ax, 4C01h           ; DOS function "terminate program" (with exit code 1)
    int 21h
io_ok:
    ; put null terminator byte after the end of the file
    mov si, dx              ; load file data pointer
    mov di, dx              ; get another pointer to start of loaded file ...
    add di, ax              ; ... plus file size
    mov byte [di], 0        ; deposit a zero there

    ; main loop
lineloop:
    lodsb                   ; load direction ...
    or al, al               ; ... check for EOF ...
    jz exit
    push ax                 ; ... and save the direction byte to the stack for now

    ; parse the number
    xor cx, cx              ; CX = number accumulator = zero for now
    mov bx, 10              ; BX = multiplier = constant 10
numloop:
    xor ax, ax              ; ensure AH = 0
    lodsb                   ; load a byte
    sub al, 30h             ; convert from ASCII to decimal
    js numend               ; if it was CR, LF or NUL, we've reached the end
    push ax                 ; save loaded value
    mov ax, cx              ; temporarily load the accumulator ...
    mul bx                  ; ... and multiply by 10 (conveniently clears DX too)
    pop cx                  ; restore the loaded value into the accumulator ...
    add cx, ax              ; ... and add the previous value (times 10)
    jmp numloop             ; ready for the next digit!
numend:
    dec si                  ; re-examine the previous byte again next time

    ; prepare evaluation of the line
    mov ax, cx              ; compute divmod 100 of the number
    mov bx, 100
    div bx                  ; note: DX is still zero from the MULs before
    ; now: DX = parsed number of clicks (mod 100)
    mov cx, word [part2]    ; load the part 2 result ...
    add cx, ax              ; ... and add the number of round-trips to it
    mov al, byte [pos]      ; load position into AL (we're going to need it soon)
    pop bx                  ; restore direction code ...
    cmp bl, 'R'             ; ... and branch on it
    je right
    ; fall-through to 'left' scenario

    ; LEFT rotation
left:
    mov ah, al              ; save original position
    sub al, dl              ; decrease position by parsed number (mod 100)
    jg .noscore             ; if > 0, no score
    or ah, ah               ; if the *original* position was 0, no score either
    jz .noscore
    inc cx                  ; all conditions fulfilled, increment part 2 score
.noscore:
    or al, al               ; check new position
    jns linedone            ; if >= 0, it's fine
    add al, 100             ; otherwise (< 0), add 100
    jmp linedone

    ; RIGHT rotation
right:
    add al, dl              ; increase position by parsed number (mod 100)
    cmp al, 100             ; if < 100, no score (and no adjustment either)
    jb .nooverflow
    sub al, 100             ; otherwise, adjust for mod-100 ...
    inc cx                  ; ... and increment part 2 score
.nooverflow:
    ; fall-through to 'linedone'

    ; finalize line
linedone:
    mov byte [pos], al      ; store final position
    mov word [part2], cx    ; store part 2 result
    or al, al               ; increment part 1 result if we are at position zero
    jnz eol
    inc word [part1]

    ; skip end-of-line characters and loop to next line
eol:
    lodsb
    cmp al, 10              ; LF? then go to the next line
    je lineloop
    or al, al               ; NUL? then EOF, else read the next byte
    jnz eol

    ; output results and exit the program
exit:
    mov ax, word [part1]    ; output part 1 result
    call OutputWord
    mov ax, word [part2]    ; output part 2 result
    ; fall-through into OutputWord -- the RET in there will exit the program

; -----------------------------------------------------------------------------
; FUNCTION: OutputWord - output a word in decimal onto the screen
; in AX = word to output
; clobbers BX, CX, DX
OutputWord:
    ; add terminating EOL to output stack
    mov bx, 10              ; LF - also doubles as quotient for the following DIVs
    push bx
    mov dl, 13
    push dx

.nextdigit:
    xor dx, dx              ; clear upper part
    div bx                  ; divide
    add dl, '0'             ; convert remainder into ASCII
    push dx                 ; ... and store to output stack
    or ax, ax               ; another iteration if value is still nonzero
    jnz .nextdigit

    ; flush output stack
    mov ah, 2               ; DOS function "write character"
.outchar:
    pop dx
    int 21h
    cmp dl, bl              ; did we already output the final LF?
    jne .outchar

    ret

; -----------------------------------------------------------------------------
; DATA SECTION

pos:   db 50    ; current position
part1: dw 0     ; part 1 result
part2: dw 0     ; part 2 result

; input filename; gets overwritten with file data during runtime
file: db "INPUT.TXT", 0
