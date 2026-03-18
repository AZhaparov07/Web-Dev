n = int(input())
x = 0
while(x < n):
    if 2**x < n:
        print(2**x)
        x += 1