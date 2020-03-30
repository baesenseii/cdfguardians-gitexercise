section .text
global _start

_start:
  mov edx, len ;length of message
  mov ecx, msg ;message to write
  mov ebx, 1 ;file descriptor (stdout)
  mov eax, 4 ;system call number (sys_write)
  int 0x80 ;call kernal

  mov eax, 1; sys_exit
  int 0x80

section .data
msg db 'Hello World!', 0xa
len equ $ - msg ;length of string
