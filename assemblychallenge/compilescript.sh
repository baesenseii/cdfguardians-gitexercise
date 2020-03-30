#!/bin/sh

read -p "enter .asm filename:" filename

echo "compiling"

nasm -f elf32 $filename.asm -o $filename.o

ld -m elf_i386 $filename.o -o $filename
