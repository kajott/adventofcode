; yasm -fbin -oaoc25_03.com aoc2025_03.asm && dosbox aoc25_03.com
; yasm -fbin -oaoc25_03.com aoc2025_03.asm && dosbox -c "mount c: $HOME/Downloads" -c "mount d: ." -c "d:" -c "c:td aoc25_03.com"

BITS 16
CPU  8086
ORG  100h

; constants
SumLen  EQU 16              ; length of a sum accumulator in pure digits
SumSize EQU SumLen+3        ; size of a sum accumulator, including the terminator bytes (CR LF $)

    ; open file
    mov ax, 3D00h           ; DOS function "open file" (for reading)
    mov dx, filename
    int 21h
    jc io_err
    mov bx, ax              ; save file handle for next operation

    ; read file contents into the (nearly) 64k of empty space in this .COM file
    mov ah, 3Fh             ; DOS function "read file"
    mov dx, filedata
    mov cx, sp              ; read as much as we (somewhat) safely can without hitting the stack
    sub cx, dx
    int 21h
    jnc io_ok
io_err:
    mov ax, 4C01h           ; DOS function "terminate program" (with exit code 1)
    int 21h
io_ok:
    ; put null terminator byte after the end of the file
    mov di, dx              ; get a pointer to start of loaded file ...
    add di, ax              ; ... plus file size
    mov byte [di], 0        ; deposit a zero there

    ; clear accumulators (fill with zeros, add terminators)
    mov di, result1         ; load pointer to the first of the ...
    mov ah, 4               ; ... FOUR result blocks
.clear:
    mov cx, SumLen          ; generate (SumLen) zeroes ...
    mov al, '0'
    rep stosb
    mov al, 13              ; ... followed by CR ...
    stosb
    mov al, 10              ; ... followed by LF ...
    stosb
    mov al, '$'             ; ... followed by a dollar sign (for int21h func 9)
    stosb
    dec ah                  ; fill the next block
    jnz .clear

    ; main line loop (SI = pointer to current line)
    mov si, dx              ; reload file data pointer
lineloop:

    ; scan for end of the digit string
    mov word [linestart], si; store line start pointer
.eodscan:
    lodsb                   ; examine a byte
    and al, 70h             ; not a control character? then loop
    jnz .eodscan
    dec si                  ; rewind to the line end
    mov word [lineend], si  ; store line end for later

    ; call the main solve function for part 1
    mov di, result1+SumLen-2
    mov al, 1
    mov bp, sum1+SumLen-1
    call Solve

    ; call the main solve function for part 2
    mov di, result2+SumLen-12
    mov al, 11
    mov bp, sum2+SumLen-1
    call Solve

    ; end of line - scan for the next line
    mov si, word [lineend]  ; restore the line end pointer
.eolscan:
    lodsb                   ; examine a byte
    or al, al               ; null terminator? then exit
    jz exit
    and al, 30h             ; a digit again? if not, loop
    jz .eolscan
    dec si                  ; rewind to line start
    jmp lineloop            ; process next line

    ; output results and exit the program
exit:
    mov si, sum1
    call OutputDigits
    mov si, sum2
    ; run right into OutputDigits, which will exit the program for us

; -----------------------------------------------------------------------------
; FUNCTION: OutputDigits - output a string of digits (must be terminated with CR LF $)
; in SI = digit string to output
; clobbers AX, DX
OutputDigits:
    ; skip leading zeros
    lodsb                   ; load a byte
    cmp al, '0'             ; if it's zero, loop
    je OutputDigits
    dec si                  ; put last examined (non-zero) byte back
    mov ah, 9               ; DOS function "write dollar-terminated string"
    mov dx, si              ; (expects pointer in DX, for whatever reason)
    int 21h
    ret

; -----------------------------------------------------------------------------
; FUNCTION: Solve - the main algorithm
; in [linestart] = start of line
; in [lineend]   = end of line
; in DI          = result to populate
; in AL          = number of digits to search (minus 1)
; in BP          = pointer to end of the sum (i.e. sum1/sum2 + SumLen - 1)
; clobbers all registers
Solve:
;    push di                 ; save original result pointer (only for outputting the finished number!)
    mov dx, [lineend]       ; DX = line end pointer
    xor ah, ah              ; subtract number of digits from it
    sub dx, ax
    mov si, [linestart]     ; SI = start of maximal substring

    ; search local maximum
    ; AH = best digit (must be zero at this point); BX = best digit position (plus 1)
.maxscan:
    lodsb                   ; load the next digit
    cmp al, ah              ; greater than the current maximum?
    jle .notmax             ; if not, don't store it
    mov ah, al              ; otherwise, store the digit ...
    mov bx, si              ; ... and its location
.notmax
    cmp si, dx              ; already at the end of the scan?
    jne .maxscan            ; if not, examine the next digit

    ; scan completed -> store digit and continue with next one
    mov al, ah              ; store the maximum digit
    stosb
    mov si, bx              ; at next iteration, start *after* this round's maximum digit
    xor ah, ah              ; reset the maximum digit for a fresh scan
    inc dx                  ; allow one extra digit to be scanned
    cmp dx, [lineend]       ; another round to go?
    jbe .maxscan            ; if so, loop again

    ; output finished number (only for testing)
;    pop si
;    call OutputDigits

    ; perform ripple-carry decimal addition
    mov cx, SumLen          ; go on for as many digits as SumLen says
    mov si, di              ; the current line's result used to be DI, is now SI
    dec si                  ; ... and it pointed one byte too far; adjust!
    mov di, bp              ; point to the destination sum
    xor ah, ah              ; AH = carry "flag" = cleared for now
    std                     ; we're going backwards
.add:
    lodsb                   ; load current line's digit
    and al, 0Fh             ; convert ASCII to number
    add al, [di]            ; add sum's digit ...
    add al, ah              ; ... and carry
    cmp al, '9'             ; did we generate a carry?
    ja .carry
    xor ah, ah              ; no carry generated
    jmp .enddigit
.carry:
    mov ah, 1               ; carry generated
    sub al, 10              ; adjust result digit
.enddigit:
    stosb                   ; store result digit
    loop .add               ; advance to the next digit
    cld                     ; restore the D flag to avoid havoc

    ret                     ; that's it!

; -----------------------------------------------------------------------------
; DATA SECTION

; input filename; gets overwritten with other stuff during runtime
filename: db "INPUT.TXT", 0

linestart EQU filename          ; pointer to start of line
lineend   EQU linestart+2       ; pointer to end of line (first byte *after* the digit string)
result1   EQU lineend+2         ; part 1 line result
sum1      EQU result1+SumSize   ; part 1 final sum
result2   EQU    sum1+SumSize   ; part 1 line result
sum2      EQU result2+SumSize   ; part 1 final sum
filedata  EQU    sum2+SumSize   ; file data
