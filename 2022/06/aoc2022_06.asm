; yasm -fbin -oaoc22_06.com aoc2022_06.asm && dosbox aoc22_06.com
; yasm -fbin -oaoc22_06.com aoc2022_06.asm && dosbox -c "mount c: $HOME/Downloads" -c "mount d: ." -c "d:" -c "c:td aoc22_06.com"

BITS 16
CPU  8086
ORG  100h

; local variables; these will overwrite the initial part of the code
bss     EQU $
hist    EQU bss         ; floating histogram data (32 bins, enough to discern letters)
bss_end EQU hist + 32   ; end of BSS section

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
    mov bp, dx          ; save loaded file offset for later

    ; close file (optional - the OS will clean up our mess too, if needed :)
;    mov ah, 3Eh         ; DOS function "close file"
;    int 21h

    ; now solve the parts!
    mov cx, 4           ; part 1
    call ScanData
    mov cx, 14          ; part 2
    ; run right into ScanData, which will also exit the program

; -----------------------------------------------------------------------------
; FUNCTION: ScanData - solve one part of the puzzle
; in CX = number (N) of consecutive bytes that need to be different
; in BP = pointer to input data
; clobbers everything except BP
ScanData:
    ; clear histogram
    push cx             ; save N while clearing the histogram
    mov bx, hist        ; we need the histogram pointer in BX later; load it now
    mov di, bx          ; clear the histogram
    mov cx, 16
    xor ax, ax
    rep stosw
    pop cx              ; restore N

    ; prepare scanning loop
    mov si, bp          ; load data pointer
    mov dx, cx          ; set "number of distinct bytes missing" (D) = N
.scanloop:

    ; scanning loop - part 1: decrement "tail"
    sub si, cx          ; point to tail (not head)
    cmp si, bp          ; still valid? (must not point before start of file)
    jb .notail          ; if not: don't process tail now
    mov al, [si]        ; load byte
    and al, 31          ; DI = AL & 31
    xor ah, ah
    mov di, ax
    dec byte [bx+di]    ; decrement slot
    jnz .notail         ; arrived at zero?
    inc dx              ; if so, increment D
.notail:
    add si, cx          ; point back to head

    ; scanning loop - part 2: increment "head"
    lodsb               ; load byte and increment pointer
    and al, 31          ; DI = AL & 31
    xor ah, ah
    mov di, ax
    mov al, [bx+di]     ; increment slot
    inc ax
    mov [bx+di], al
    dec ax              ; seen the first time?
    jnz .scanloop       ; no -> continue with next byte
    dec dx              ; yes -> decrement D
    jnz .scanloop       ; loop again if we've not found enough distinct bytes

    ; hit found -> compute offset and output it
    mov ax, si
    sub ax, bp
    ; now run right into the OutputWord function which will also return

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

; input filename; gets overwritten with file data later
file: db "INPUT.TXT", 0
