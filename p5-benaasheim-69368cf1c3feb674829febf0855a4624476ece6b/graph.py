from stack_array import * #Needed for Depth First Search
from queue_array import * #Needed for Breadth First Search

class Vertex:
    '''Add additional helper methods if necessary.'''
    def __init__(self, key):
        '''Add other attributes as necessary'''
        self.id = key
        self.adjacent_to = []
        self.color = " "
    def __repr__(self):
        return "{0}|{1}".format(self.id, self.color)

class Graph:
    '''Add additional helper methods if necessary.'''
    def __init__(self, filename):
        '''reads in the specification of a graph and creates a graph using an adjacency list representation.
           You may assume the graph is not empty and is a correct specification.  E.g. each edge is
           represented by a pair of vertices.  Note that the graph is not directed so each edge specified
           in the input file should appear on the adjacency list of each vertex of the two vertices associated
           with the edge.'''
        self.verts = []

        try:
            a = open(filename, "r")
            lines = a.readlines()
            a.close()
        except:
            raise FileNotFoundError()
        for x in lines:
            i = x.split(" ")
            self.add_vertex(i[0])
            self.add_vertex(i[1][:-1])
            if (i[0] != i[1]) and (i[0] != None) and (i[1] != None):
                v1 = self.get_vertex(i[0])
                v2 = self.get_vertex(i[1][:-1])
                self.add_edge(v1, v2)

    def add_vertex(self, key):
        '''Add vertex to graph, only if the vertex is not already in the graph.'''
        vertex = Vertex(key)
        if self.get_vertex(key) == None:
            self.verts.append(vertex)

    def get_vertex(self, key):
        '''Return the Vertex object associated with the id. If id is not in the graph, return None'''
        for i in self.verts:
            if i.id == key:
                return i
        return None

    def add_edge(self, v1, v2):
        '''v1 and v2 are vertex id's. As this is an undirected graph, add an
           edge from v1 to v2 and an edge from v2 to v1.  You can assume that
           v1 and v2 are already in the graph'''
        (v1.adjacent_to).append(v2)
        (v2.adjacent_to).append(v1)

    def get_vertices(self):
        '''Returns a list of id's representing the vertices in the graph, in ascending order'''
        retlis = []
        for i in self.verts:
            retlis.append(i.id)
        retlis.sort()
        return retlis

    def get_verts(self):
        '''Returns a list of id's representing the vertices in the graph, in ascending order'''
        return self.verts

    def conn_components(self):
        '''Returns a list of lists.  For example, if there are three connected components
           then you will return a list of three lists.  Each sub list will contain the
           vertices (in ascending order) in the connected component represented by that list.
           The overall list will also be in ascending order based on the first item of each sublist.
           This method MUST use Depth First Search logic!'''
        vlis = self.get_verts()
        vstack = Stack(len(vlis))
        retlis = []
        for i in vlis:
            check1 = False
            for n in retlis:
                if i.id in n:
                    check1 = True
            if not check1:
                temp = []
                temp.append(i.id)
                for s in i.adjacent_to:
                    vstack.push(s)
                while not vstack.is_empty():
                    tempe = vstack.pop()
                    if tempe.id not in temp:
                        for m in tempe.adjacent_to:
                            vstack.push(m)
                        temp.append(tempe.id)
                temp.sort()
                retlis.append(temp)
        return retlis

    def is_bipartite(self):
        '''Returns True if the graph is bicolorable and False otherwise.
           This method MUST use Breadth First Search logic!'''
        vlis = self.get_verts()
        vque = Queue(len(vlis))
        retlis = []
        for i in vlis:
            vque.enqueue(i)
        while vque.num_items > 0:
            print(vque.num_items, vque.items)
            x = vque.dequeue()
            for i in x.adjacent_to:
                if (i.color == x.color) and (x.color != " "):
                    return False
                elif i.color == " ":
                    i.color = "B"
                    if x.color == "B":
                        i.color = "R"
            if x.color == " ":
                vque.enqueue(x)
        return True
