a = int(input())
b = int(input())
c = int(input())
d = int(input())
def min(a,b,c,d):
    if((a < b) and (a < c) and (a < d)):
        return a
    elif((b < a) and (b < c) and (b < d)):
        return b
    elif((c < b) and (c < a) and (c < d)):
        return c
    elif((d < b) and (d < c) and (d < a)):
        return d
print(min(a,b,c,d))