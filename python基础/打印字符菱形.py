n = 5
char = '*'

for i in range(n // 2 + 1):
   print(' ' * (n // 2 - i) + char * (2 * i + 1))

for i in range(n // 2 - 1, -1, -1):
    print(' ' * (n // 2 - i) + char * (2 * i + 1))