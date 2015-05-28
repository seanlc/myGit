TITLE Program Template (Template.asm)
; Program Description: Print Fibonacci until Overflow
; Author: Sean Carstensen
; Creation Date: 5/28/2015
; Revisions:
; Status: Complete
;Modified by:
INCLUDE Irvine32.inc
.data
; (insert variables here)
newline byte 0ah,0dh, 0
.code
main PROC
; (insert executable instructions here)
mov eax, 1	
mov ebx, 1
call WriteInt

mov edx, offset newline
call WriteString

call WriteInt
call WriteString

L1: mov ecx, eax		; preserve last value in ecx
	add eax, ebx		; obtain new value by adding n-1 to n
	jc next				; if an overflow occurs exit
	Call WriteInt		; write integer to output
	Call WriteString	; write newline
	mov ebx, ecx		; mov last value to ebx for next iteration
	jmp L1
next:
exit
main ENDP
; (insert additional procedures here)
END main