import sys as sys_c

val = False
if val and True:
    print("hello AND world")
if val or True:
    print(f"hello OR world. version: {sys_c.version}")

assert val == False
i = 0
while True:
    if i == 10:
        break
    print(f"index{i}")
    i += 1


class Simple:
    def simple_print(self):
        print("simple_print is called")


simple = Simple()
# del simple
simple.simple_print()
