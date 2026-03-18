n = int(input())
y = 0
t = 0
while(y < n):
    if(2**y == n):
        t += 1
    y += 1
if t == 0:
    print("NO")
else:
    print("YES")