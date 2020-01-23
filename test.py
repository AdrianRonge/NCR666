
def function(a, b):
    a = int(a)
    b = int(b)
    c = int(b - a)
    d = []
    a = a + 1
    while (c > 0):
        if (a == 1 or a == 2 or a == 3 or a == 5 or a == 7):
            d.append(a)
        else:
            if (a%2 != 0 and a%3 != 0 and a%5 != 0 and a%7 != 0):
                d.append(a)
        a = a + 1
        c = c - 1
    for i in d:
        print(str(i))

function(2, 21)