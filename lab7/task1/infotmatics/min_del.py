x = int(input())
y = 2
while(y < x):
    if x % y == 0:
        print(y)
        break
    y+=1