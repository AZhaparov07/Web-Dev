x = int(input())
y = int(input())
for i in range(x,y):
    if(pow(i,2) > x) and (pow(i,2) < y):
        print(pow(i,2), end=' ')