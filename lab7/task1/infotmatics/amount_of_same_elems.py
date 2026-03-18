n = int(input())
list = []
counter = 0
for i in range(n):
    num = int(input())
    list.append(num)
for i in range(n):
    if list[i] > 0:
        counter += 1
print(counter)