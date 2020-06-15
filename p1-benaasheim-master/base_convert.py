def g(a,b):
    rems = []
    qot = a // b
    rem = a % b
    print(qot, rem)
    rems.append(rem)
    if qot != 0:
        rams = g(qot,b)
        rams.append(rems[0])
        rems = rams
    return rems

def convert(a,b):
    rems = g(a,b)
    string = ""
    for i in rems:
        if i > 9:
            string += chr(i + 55)
        else:
            s = str(i)
            string += s
    return string


