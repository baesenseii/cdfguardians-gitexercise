//create a while loop with jumps and labels

global_start

_start:
  mov EAX, 1
  mov EBX, 0
  mov ECX, 10
  jmp loop

loop:
inc EBX
cmp EBX, ECX ;takes EBX - ECX and compares the value
jne loop ;restarts the loop if ebx
int 0x80
