x = int(input())
y = int(input())
c = int(input())
d = int(input())
for i in range(x,y):
    if i % d == c:
        print(i, end=' ')
