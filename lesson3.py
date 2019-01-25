a = input().split('.')
c = int(input())
b = a[1][:c]
u = a[0][:c]
d = ''
if a[0] == '0':
    x = list(a[1])
    g = int(x[c])
    if g >= 5:
        print(1)
    else:
        print(0)
else:
    d = ''
    if c > len(a[1]):
        b += (c - len(a[1]))*'0'
    elif c < len(a[1]):
        x = list(a[1])
        g = int(x[c])
        y = list(a[0])
        if g >= 5:
            if c == 0:
                u = 1
                o = 1
            else:
                x[c-1] = str(int(x[c-1]) + 1)
                b = ''.join(x)[:c]
    elif c == len(a[1]):
         a[1] += '0'
    if c != 0:
        d = a[0] + '.' + b
    elif c == 0 and o != 1:
        d = a[0]
    elif o == 1:
        d = int(a[0]) + u
    print(d)