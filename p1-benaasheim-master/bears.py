def bears(b):
    if b == 42:
        return True
    pos = []
    if ((b % 4 == 0) or (b % 3 == 0)) and b > 42:
        x = str(b)
        y = int(x[len(x)-1:])
        z = int(x[len(x)-2:len(x)-1])
        pos.append(b - (y * z))
    if b % 2 == 0:
        pos.append(b//2)
    if b % 5 == 0:
        pos.append(b-42)
    #print(pos)
    #x = input("")
    for i in pos:
        if i == 42:
            return True
        elif (i != b) and (i >= 42):
            if bears(i):
                return True
    return False

print(bears(250))
