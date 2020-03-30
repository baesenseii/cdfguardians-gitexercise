global _start

_start:
	mov EAX, 1
	mov ECX, 3
	cmp EAX, ECX
	jg label
	mov EBX, 42
	int 0x80

label:
	mov EBX, 25
	int 0x80
