global _start

_start:
	mov EBX, 42
	mov EAX, 1 ;system exit call (prints the value of EBX)

	int 0x80
