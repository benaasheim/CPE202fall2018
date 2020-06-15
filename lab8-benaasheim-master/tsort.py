from sys import argv
from stack_array import *
from operator import itemgetter

def tsort(vertices):
    '''
    * Performs a topological sort of the specified directed acyclic graph.  The
    * graph is given as a list of vertices where each pair of vertices represents
    * an edge in the graph.  The resulting string return value will be formatted
    * identically to the Unix utility {@code tsort}.  That is, one vertex per
    * line in topologically sorted order.
    *
    * Raises a ValueError if:
    *   - vertices is emtpy with the message "input contains no edges"
    *   - vertices has an odd number of vertices (incomplete pair) with the
    *     message "input contains an odd number of tokens"
    *   - the graph contains a cycle (isn't acyclic) with the message
    *     "input contains a cycle"'''
    a = f1(vertices)
    a = sortr(a)
    f2(a)
    a = sortr(a)
    ss = Stack(len(a))
    f43(a, ss, vertices)
    a = sortr(a)
    if ss.num_items == 0:
        raise ValueError("input contains a cycle")
    rlis = f4(a, ss, vertices)
    rstr = ""
    for i in rlis:
        rstr += i + "\n"
    return rstr

def f1(vertices):
    a = []
    if (len(vertices)%2) != 0:
        raise ValueError("input contains an odd number of tokens")
    if vertices == []:
        raise ValueError("input contains no edges")
    for n in range(0, len(vertices)):
        if (n%2) == 0:
            if vertices[n] == "":
                raise ValueError("input contains no edges")
            inn = False
            for i in a:
                if (i != None) and (i[0] == vertices[n]):
                    inn = True
                    i[2].append(vertices[n+1])
            if not inn:
                c = []
                c.append(vertices[n+1])
                temp = [vertices[n], 0, c]
                a.append(temp)
        else:
            if vertices[n] == "":
                raise ValueError("input contains no edges")
            inn = False
            for i in a:
                if (i != None) and (i[0] == vertices[n]):
                    inn = True
            if not inn:
                c = []
                temp = [vertices[n], 0, c]
                a.append(temp)
    return a

def f2(a):
    for i in a:
        for n in a:
            for s in n[2]:
                if i[0] == s:
                    i[1] += 1

def f3(a, ss):
    for i in a:
        if i[1] == 0:
            ss.push(i)
    if ss.num_items == 0:
        raise ValueError("input contains a cycle")

def f4(a, ss, vertices):
    rlis = []
    alen = len(a)
    while ss.num_items > 0:
        a = sortr(a)
        temp = ss.pop()
        rlis.append(temp[0])
        if len(a) > 0:
            f42(temp, a)
        f43(a, ss, vertices)
    cc(ss, a)
    return rlis

def cc(ss, a):
    if ccheck(ss, a) == False:
        raise ValueError("input contains a cycle")

def ccheck(ss, a):
    if (ss.num_items == 0) and (len(a) > 0):
        return False
    else:
        return True

def f42(temp, a):
    done = False
    cc = 0
    while done == False:
        if (cc) == len(a):
            done = True
        else:
            if a[cc][1] == 0:
                a.remove(a[cc])
            else:
                cc += 1
    for i in temp[2]:
        for n in range(len(a)):
            if (a[n] != None) and (i == a[n][0]):
                a[n][1] -= 1

def f43(a, ss, vertices):
    new = []
    for i in a:
        if (i[1] == 0):
            new.append(i)
    for i in vertices:
        for n in new:
            if i == n[0]:
                ss.push(n)
                new.remove(n)

def sortr(a):
    new = []
    while len(a) > 0:
        lowest = a[0]
        for i in a:
            try:
                if int(i[0]) < int(lowest[0]):
                    lowest = i
            except:
                if i[0] < lowest[0]:
                    lowest = i
        new.append(lowest)
        a.remove(lowest)
    return new

def main():
    '''Entry point for the tsort utility allowing the user to specify
       a file containing the edge of the DAG'''
    if len(argv) != 2:
        print("Usage: python3 tsort.py <filename>")
        exit()
    try:
        f = open(argv[1], 'r')
    except FileNotFoundError as e:
        print(argv[1], 'could not be found or opened')
        exit()

    vertices = []
    for line in f:
        vertices += line.split()
    f.close()
    try:
        result = tsort(vertices)
        return result
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
