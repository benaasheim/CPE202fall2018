class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char   # stored as an integer - the ASCII character code value
        self.freq = freq   # the freqency associated with the node
        self.left = None   # Huffman tree (node) to the left
        self.right = None  # Huffman tree (node) to the right
        self.key = ""
    def __repr__(self):
        return "{0}|{1}".format(self.char, self.freq)
    def NLR(self, q, key):
        if self.left == None:
            if self.right == None:
    #            print([self.char, (key+self.key)])
                q.append((self.char, (key+self.key)))
        else:
            if self.right != None:
                self.left.NLR(q, (key+self.key))
                self.right.NLR(q, (key+self.key))

def comes_before(a, b):
    """Returns True if tree rooted at node a comes before tree rooted at node b, False otherwise"""
    if a.freq < b.freq:
        return True
    elif a.freq > b.freq:
        return False
    else:
        if a.char < b.char:
            return True
        else:
            return False

def combine(a, b):
    """Creates and returns a new Huffman node with children a and b, with the "lesser node" on the left
    The new node's frequency value will be the sum of the a and b frequencies
    The new node's char value will be the lesser of the a and b char ASCII values"""
    if b.char < a.char:
        x = HuffmanNode((b.char), (a.freq + b.freq))
    else:
        x = HuffmanNode((a.char), (a.freq + b.freq))
    x.left = a
    a.key = "0"
    x.right = b
    b.key = "1"
    return x

def cnt_freq(filename):
    """Opens a text file with a given file name (passed as a string) and counts the
    frequency of occurrences of all the characters within that file"""
    a = open(filename, "r")
    lines = a.readlines()
    a.close()
    lones = []
    frelis = [0]*256
    for i in lines:
        for n in i:
            frelis[(ord(n))] += 1
    return frelis

def create_huff_tree(frelis):
    """Create a Huffman tree for characters with non-zero frequency
    Returns the root node of the Huffman tree"""
    nodelis = []
    for n in range(len(frelis)):
        if frelis[n] > 0:
            nodelis.append(HuffmanNode(n, frelis[n]))
    Huffman_Sort(nodelis)
    while len(nodelis) > 1:
    #    print(nodelis)
        nodelis.append(combine(nodelis[0], nodelis[1]))
        nodelis = nodelis[2:]
        Huffman_Sort(nodelis)
    return nodelis[0]

def create_code(node):
    """Returns an array (Python list) of Huffman codes. For each character, use the integer ASCII representation
    as the index into the arrary, with the resulting Huffman code for that character stored at that location"""
    codes = [None]*256
    q = []
    node.NLR(q, "")
    for i in q:
        x = i
        codes[x[0]] = x[1]
    return codes

def create_header(freqs):
    """Input is the list of frequencies. Creates and returns a header for the output file
    Example: For the frequency list asscoaied with "aaabbbbcc, would return “97 3 98 4 99 2” """
    header = ""
    for n in range(len(freqs)):
        if freqs[n] != 0:
            header += str(n) + " " + str(freqs[n]) + " "
    return header[0:-1]

def Huffman_Sort(nlis):
    placemark = 0
    while placemark < len(nlis):
        lowest = nlis[placemark]
        lowin = placemark
        for s in range(lowin, len(nlis)):
            if comes_before(nlis[s], lowest):
                lowest = nlis[s]
                lowin = s
        a = nlis[placemark]
        nlis[placemark] = lowest
        nlis[lowin] = a
        placemark += 1

def make_code(codes, filename):
    a = open(filename, "r")
    lines = a.readlines()
    a.close()
    code = ""
    if len(lines) > 1:
        for i in lines:
            for n in i:
                code += codes[ord(n)]
    else:
        for n in range(len(lines[0])):
            code += codes[ord(lines[0][n])]
    return code

def huffman_encode(in_file, out_file):
    """Takes inout file name and output file name as parameters
    Uses the Huffman coding process on the text from the input file and writes encoded text to output file
    Take not of special cases - empty file and file with only one unique character"""
    frelis = cnt_freq(in_file)
    hufftree = create_huff_tree(frelis)
    header = create_header(frelis)
    codes = create_code(hufftree)
    code = make_code(codes, in_file)
    b = open(out_file, "w+")
    b.write(header + "\n")
    b.write(code)
    b.close()

def parse_header(header):
    lof = [0]*256
    a = header.split(" ")
    for n in range(0, len(a), 2):
        lof[int(a[n])] = int(a[n+1])
    return lof

def code_2_script(code, hufftree):
    script = ""
    n = 0
    temp = hufftree
    while n < len(code):
        if code[n] == "0":
            if temp.left == None:
                script += chr(temp.char)
                temp = hufftree
            else:
                temp = temp.left
                n += 1
        else:
            if temp.right == None:
                script += chr(temp.char)
                temp = hufftree
            else:
                temp = temp.right
                n += 1
    return script

def huffman_decode(encoded_file, decoded_file):
    try:
        a = open(encoded_file, "r")
        lines = a.readlines()
        a.close()
    except:
        raise FileNotFoundError("FileNotFoundError")
    script = ""
    if len(lines) == 0:
        script = ""
    elif len(lines) == 1:
        script = ""
        print(lines[0])
        x = lines[0].split(" ")
        print(x)
        for i in range(int(x[1])):
            script += chr(int(x[0]))
    else:
        script = ""
        list_of_freqs = parse_header(lines[0])
        hufftree = create_huff_tree(list_of_freqs)
        script = code_2_script(lines[1], hufftree)
    b = open(decoded_file, "w+")
    b.write(script)
    b.close()
