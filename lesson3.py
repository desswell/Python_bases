
a = input().split('.')
c = int(input())
b = a[1][:c]
d = ''
if c > len(a[1]):
    b += (len(a[1]) - 2)*'0'
    d = ''
elif c < len(a[1]):
    x = list(a[1])
    g = int(x[c])
    if g >= 5:
        x[c-1] = str(int(x[c-1]) + 1)
    b = ''.join(x)[:c]
elif c == len(a[1]):
    a[1] += '0'
if c != 0:
    d = a[0] + '.' + b
else:
    d = a[0]
print(d)