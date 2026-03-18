n = int(input())
t = 0
while(t <= n):
    if 2**t >= n:
        print(t)
        break
    t += 1