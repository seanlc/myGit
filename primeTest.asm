TITLE Program Template (Template.asm)
; Program Description: Prime Number Test
; Author: Sean Carstensen
; Creation Date: 5/28/2015
; Revisions:
; Status: Incomplete
;Modified by:
INCLUDE Irvine32.inc
.data
prompt byte "Enter the number you suspect of being prime (-1 to exit): ",0
primeanswer byte " is prime",0
notprimeanswer byte " is not prime",0
number dword ?
newline byte 0dh,0ah,0
currentTest dword ?
.code
main PROC
top:
lea edx, prompt
Call WriteString
Call ReadInt		;prompt user for a number to test
mov number, eax

cmp eax, -1
je norepeat			; exit program if input is -1

mov ebx, 2			; 2 is the first divisor to be tested and is put in ebx
L1:	cmp ebx, eax	; if divisor has reached dividend, the number is prime
	jge prime		; go to prime block

	mov edx, 0		; clear upper half of divisor
	div ebx			
	cmp edx, 0		; compare remainder to 0
	je notprime		; if remainder = 0, jump to prime block
	inc ebx			; otherwise increment the divisor
	mov eax, number	; restor the test number to eax
	jmp L1			;	and run loop again


prime:
lea edx, primeanswer
mov eax, number
Call WriteInt
Call WriteString
jmp next		; tells the user that their number is prime

notprime:
lea edx, notprimeanswer
mov eax, number
Call WriteInt
Call WriteString		; tells the user that their number is not prime

next:
lea edx, newline
Call WriteString


jmp top			; repeat program

norepeat:
exit
main ENDP

END main