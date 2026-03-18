n = int(input())
list = []
for i in range(n):
    num = int(input())
    list.append(num)
for i in range(n):
    if i % 2 == 0:
        print(list[i], end=' ')