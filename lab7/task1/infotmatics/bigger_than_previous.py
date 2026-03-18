n = int(input())
list = []
counter = 0
for i in range(n):
    num = int(input())
    list.append(num)
for i in range(n-1):
    if list[i+1] > list[i]:
        counter += 1
print(counter)