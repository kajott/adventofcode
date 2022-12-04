; yasm -fbin -oaoc22_03.com aoc2022_03.asm && dosbox aoc22_03.com
; yasm -fbin -oaoc22_03.com aoc2022_03.asm && dosbox -c "mount c: ." -c "c:" -c "td aoc22_03.com"

BITS 16
CPU  8086
ORG  100h

; local variables; these will overwrite the initial part of the code
bss     EQU $
half1   EQU bss         ; first half's bitfield
half2   EQU half1 + 8   ; second half's bitfield
accum   EQU half2 + 8   ; line accumulator for second part
part1   EQU accum + 8   ; part 1 result
part2   EQU part1 + 2   ; part 2 result
lnmod3  EQU part2 + 2   ; line number mod 3
bss_end EQU lnmod3 + 1  ; end of BSS section

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

    ; clear local variables
    mov [part1], ax
    mov [part2], ax
    mov [lnmod3], al

    ; iterate over the input file
nextline:
    ; check and increment line counter
    mov dl, [lnmod3]
    or dl, dl
    jnz .noreset
    mov di, accum       ; clear 'accum' every third line
    mov ax, 0FFFFh
    stosw
    stosw
    stosw
    stosw
.noreset:
    inc dl              ; increase line counter (will now be zero at the *end* of a 3-line group)
    cmp dl, 3
    jb .nowrap
    xor dl, dl
.nowrap:
    mov [lnmod3], dl

    ; scan the current line
    mov di, si          ; mark the start of the current line
nextbyte:
    lodsb
    or al, al           ; EOF reached?
    jz eof
    cmp al, 0Ah         ; EOL reached?
    jnz nextbyte

    ; end of line reached
    mov cx, si          ; calculate half of the line length
    sub cx, di
    shr cx, 1
    push si             ; save current input position
    ; generate bitfield for the first half of the line
    mov si, di          ; input pos = start of line
    push cx             ; save a few registers
    push di
    mov bx, half1       ; scan into first half bitfield
    call StringToBitfield
    ; generate bitfield for the second half of the line
    pop si              ; restore start of line (as current pos) and counter
    pop cx
    add si, cx          ; go to second half of the line
    mov bx, half2       ; scan into second half bitfield
    call StringToBitfield
    ; done generating bitfields

    ; coalesce bitfields:
    ; - half1 = half1 AND half2  [intersection of halves, for part 1]
    ; - accum = accum AND (half1 OR half2)  [intersection of union of halves, for part 2]
    mov bx, half1       ; set pointer
.cbloop:
    mov ax, [bx]        ; load all words
    mov cx, [bx+8]
    mov dx, [bx+16]
    mov di, cx          ; backup one of the halves
    or  cx, ax          ; temp = half1 OR half2
    and ax, di          ; half1 = half1 AND half2
    and dx, cx          ; accum = accum OR temp
    mov [bx], ax        ; store both results
    mov [bx+16], dx
    add bx, 2           ; continue with next word
    cmp bx, half2
    jne .cbloop

    ; evaluate part 1
    mov si, half1
    call ScanBitfield
    add [part1], cx

    ; evaluate part 2 (if necessary)
    mov al, [lnmod3]
    or al, al
    jnz .nopart2
    mov si, accum
    call ScanBitfield
    add [part2], cx
.nopart2:

    ; end of all line handling
    pop si              ; restore line scanner's input position
    jmp nextline

eof:
    ; end of file, output results
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
; FUNCTION: StringToBitfield - scan a string and add the letters into a bitfield
; in SI = pointer to input data
; in BX = pointer to bitfield (will be cleared before scanning)
; in CX = number of bytes to scan
; clobbers AX, CX, SI; preserves BX
StringToBitfield:
    ; clear bitfield first
    xor ax, ax
    mov [bx], ax
    mov [bx+2], ax
    mov [bx+4], ax
    mov [bx+6], ax
    ; scan the string
.scanloop:
    lodsb
    sub al, 'a'         ; convert (and check for) lowercase character
    cmp al, 26
    jb .lowcase
    add al, 32          ; check again for uppercase character
    cmp al, 26
    jae .nochar
    add al, 26          ; add base score for uppercase characters
.lowcase:
    push cx             ; save byte counter and bitmap base
    push bx
    xor ah, ah          ; extract byte position
    mov cx, ax
    shr cx, 1
    shr cx, 1
    shr cx, 1
    add bx, cx          ; ... and add to bitmap pointer
    mov cl, al          ; extract bit position
    and cl, 7
    mov al, 1           ; generate a shifted bit
    shl al, cl
    or [bx], al         ; add to bitmap
    pop bx              ; restore byte counter and bitmap base
    pop cx
.nochar:
    loop .scanloop
    ret

; -----------------------------------------------------------------------------
; FUNCTION: ScanBitfield - detect index of first set bit in a bitfield
; in SI = pointer to bitfield
; out CX = result index, *plus 1*
; clobbers AX, BX, DX
ScanBitfield:
    xor cx, cx          ; reset counter
.scanbyte:
    lodsb               ; load a byte
    or al, al           ; any bit set?
    jnz .scanbit        ; no bits set -> skip the whole byte
    add cl, 8
    jmp .scanbyte
.scanbit:
    inc cx              ; increase counter
    shr al, 1           ; shift the value by one position
    jnc .scanbit        ; bit not set? -> continue scanning
    ret

; -----------------------------------------------------------------------------
; FUNCTION: DumpBitfield - dump a bitfield to the console [DEBUG]
; in BX = pointer to bitfield
; clobbers AX, BX, CX, DX
;DumpBitfield:
;    mov cl, 4
;    mov ah, 2
;.dumpword:
;    mov dx, [bx]
;    add bx, 2
;    mov ch, 16
;.dumpbit:
;    push dx
;    and dl, 1
;    add dl, dl
;    add dl, dl
;    add dl, dl
;    add dl, dl
;    neg dl
;    add dl, '_'
;    int 21h
;    pop dx
;    shr dx, 1
;    dec ch
;    jnz .dumpbit
;    loop .dumpword
;    mov dl, 0Dh
;    int 21h
;    mov dl, 0Ah
;    int 21h
;    ret

; -----------------------------------------------------------------------------
; DATA SECTION

; input filename; gets overwritten with file data later
file: db "INPUT.TXT", 0
