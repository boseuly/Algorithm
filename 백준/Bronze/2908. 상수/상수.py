
import sys
a,b = map(int, sys.stdin.readline().split())
a_stack, b_stack = list(map(str, str(a))),list(map(str, str(b)))
reverse_a,reverse_b  = "", ""
for _ in range(3):
    reverse_a += a_stack.pop()
    reverse_b += b_stack.pop()
if reverse_a > reverse_b:
    print(reverse_a)
else:
    print(reverse_b)