# C-950Joseph Demuth Student ID: 001253330
import importcsv

importcsv.loadPackageData('packages.csv')


# Truck class.
class Truck:
    def __init__(self, trucknumber, dhour, dminute, hour, minute, location, packages,miles):
        self.trucknumber = trucknumber
        self.dhour = int(dhour)
        self.dminute = int(dminute)
        self.hour = hour
        self.minute = minute
        self.location = location
        self.packages = packages
        self.miles = miles

    def __str__(self):  # overwite print(package) otherwise it will print object reference
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (
            self.trucknumber, self.dhour, self.dminute, self.hour, self.minute, self.location, self.miles)

    def printpackages(self):
        for i in range(len(self.packages)):
            p = importcsv.myHash.search(self.packages[i])
            print("Package(s) at ", p.address, " status is ", p.status, ".")


# Graph class.
class Graph:
    def __init__(self):
        self.adjacency_list = {}  # vertex dictionary {key:value}
        self.edge_weights = {}  # edge dictionary {key:value}

    def add_vertex(self, new_vertex):
        self.adjacency_list[new_vertex] = []  #

    def add_directed_edge(self, from_vertex, to_vertex, weight=1.0):
        self.edge_weights[(from_vertex, to_vertex)] = weight
        #
        self.adjacency_list[from_vertex].append(to_vertex)
        #

    def add_undirected_edge(self, vertex_a, vertex_b, weight=1.0):
        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)


g = Graph()  # Instantiate graph as g.


# Function to populate the graph g.
def creategraph():
    # add Vertices
    vertex_0 = 0  # HUB
    g.add_vertex(vertex_0)
    vertex_1 = 1  # 1, 195 Oakland ave
    g.add_vertex(vertex_1)
    vertex_2 = 2  # 2, 2530 S 500 E
    g.add_vertex(vertex_2)
    vertex_3 = 3  # 3, 233 Canyon RD
    g.add_vertex(vertex_3)
    vertex_4 = 4  # 4, 380 W 2880 S
    g.add_vertex(vertex_4)
    vertex_5 = 5  # 5, 410 S State St
    g.add_vertex(vertex_5)
    vertex_6 = 6  # 6, 3060 Lester St
    g.add_vertex(vertex_6)
    vertex_7 = 7  # 7, 1330 2100 S
    g.add_vertex(vertex_7)
    vertex_8 = 8  # 8, 300 State St
    g.add_vertex(vertex_8)
    vertex_9 = 9
    g.add_vertex(vertex_9)
    vertex_10 = 10
    g.add_vertex(vertex_10)
    vertex_11 = 11
    g.add_vertex(vertex_11)
    vertex_12 = 12
    g.add_vertex(vertex_12)
    vertex_13 = 13
    g.add_vertex(vertex_13)
    vertex_14 = 14
    g.add_vertex(vertex_14)
    vertex_15 = 15
    g.add_vertex(vertex_15)
    vertex_16 = 16
    g.add_vertex(vertex_16)
    vertex_17 = 17
    g.add_vertex(vertex_17)
    vertex_18 = 18
    g.add_vertex(vertex_18)
    vertex_19 = 19
    g.add_vertex(vertex_19)
    vertex_20 = 20
    g.add_vertex(vertex_20)
    vertex_21 = 21
    g.add_vertex(vertex_21)
    vertex_22 = 22
    g.add_vertex(vertex_22)
    vertex_23 = 23
    g.add_vertex(vertex_23)
    vertex_24 = 24
    g.add_vertex(vertex_24)
    vertex_25 = 25
    g.add_vertex(vertex_25)
    vertex_26 = 26
    g.add_vertex(vertex_26)

    # add Edges
    g.add_undirected_edge(vertex_0, vertex_0, 0.0)
    g.add_undirected_edge(vertex_0, vertex_1, 3.5)
    g.add_undirected_edge(vertex_0, vertex_2, 2.8)
    g.add_undirected_edge(vertex_0, vertex_3, 7.6)
    g.add_undirected_edge(vertex_0, vertex_4, 3.6)
    g.add_undirected_edge(vertex_0, vertex_5, 6.5)
    g.add_undirected_edge(vertex_0, vertex_6, 5.2)
    g.add_undirected_edge(vertex_0, vertex_7, 3.8)
    g.add_undirected_edge(vertex_0, vertex_8, 7.6)
    g.add_undirected_edge(vertex_0, vertex_9, 5.0)
    g.add_undirected_edge(vertex_0, vertex_10, 6.4)
    g.add_undirected_edge(vertex_0, vertex_11, 7.6)
    g.add_undirected_edge(vertex_0, vertex_12, 10.9)
    g.add_undirected_edge(vertex_0, vertex_13, 1.9)
    g.add_undirected_edge(vertex_0, vertex_14, 3.4)
    g.add_undirected_edge(vertex_0, vertex_15, 4.4)
    g.add_undirected_edge(vertex_0, vertex_16, 11.0)
    g.add_undirected_edge(vertex_0, vertex_17, 2.2)
    g.add_undirected_edge(vertex_0, vertex_18, 2.0)
    g.add_undirected_edge(vertex_0, vertex_19, 3.6)
    g.add_undirected_edge(vertex_0, vertex_20, 6.4)
    g.add_undirected_edge(vertex_0, vertex_21, 2.4)
    g.add_undirected_edge(vertex_0, vertex_22, 2.4)
    g.add_undirected_edge(vertex_0, vertex_23, 7.2)
    g.add_undirected_edge(vertex_0, vertex_24, 3.2)
    g.add_undirected_edge(vertex_0, vertex_25, 2.8)
    g.add_undirected_edge(vertex_0, vertex_26, 8.6)
    g.add_undirected_edge(vertex_1, vertex_1, 0)
    g.add_undirected_edge(vertex_1, vertex_2, 1.5)
    g.add_undirected_edge(vertex_1, vertex_3, 4.5)
    g.add_undirected_edge(vertex_1, vertex_4, 1.1)
    g.add_undirected_edge(vertex_1, vertex_5, 3.5)
    g.add_undirected_edge(vertex_1, vertex_6, 3.9)
    g.add_undirected_edge(vertex_1, vertex_7, 2.8)
    g.add_undirected_edge(vertex_1, vertex_8, 4.5)
    g.add_undirected_edge(vertex_1, vertex_9, 3.5)
    g.add_undirected_edge(vertex_1, vertex_10, 8.7)
    g.add_undirected_edge(vertex_1, vertex_11, 5.7)
    g.add_undirected_edge(vertex_1, vertex_12, 6.3)
    g.add_undirected_edge(vertex_1, vertex_13, 4.9)
    g.add_undirected_edge(vertex_1, vertex_14, 6.9)
    g.add_undirected_edge(vertex_1, vertex_15, 3.0)
    g.add_undirected_edge(vertex_1, vertex_16, 6.9)
    g.add_undirected_edge(vertex_1, vertex_17, 1.9)
    g.add_undirected_edge(vertex_1, vertex_18, 1.9)
    g.add_undirected_edge(vertex_1, vertex_19, 7.2)
    g.add_undirected_edge(vertex_1, vertex_20, 9.0)
    g.add_undirected_edge(vertex_1, vertex_21, 4.2)
    g.add_undirected_edge(vertex_1, vertex_22, 5.9)
    g.add_undirected_edge(vertex_1, vertex_23, 4.8)
    g.add_undirected_edge(vertex_1, vertex_24, 0.8)
    g.add_undirected_edge(vertex_1, vertex_25, 3.8)
    g.add_undirected_edge(vertex_1, vertex_26, 4.3)
    g.add_undirected_edge(vertex_2, vertex_2, 0)
    g.add_undirected_edge(vertex_2, vertex_3, 4.8)
    g.add_undirected_edge(vertex_2, vertex_4, 1.8)
    g.add_undirected_edge(vertex_2, vertex_5, 4.1)
    g.add_undirected_edge(vertex_2, vertex_6, 4.6)
    g.add_undirected_edge(vertex_2, vertex_7, 1.6)
    g.add_undirected_edge(vertex_2, vertex_8, 5.1)
    g.add_undirected_edge(vertex_2, vertex_9, 3.2)
    g.add_undirected_edge(vertex_2, vertex_10, 9.4)
    g.add_undirected_edge(vertex_2, vertex_11, 6.7)
    g.add_undirected_edge(vertex_2, vertex_12, 8.0)
    g.add_undirected_edge(vertex_2, vertex_13, 3.8)
    g.add_undirected_edge(vertex_2, vertex_14, 5.8)
    g.add_undirected_edge(vertex_2, vertex_15, 3.7)
    g.add_undirected_edge(vertex_2, vertex_16, 7.3)
    g.add_undirected_edge(vertex_2, vertex_17, 2.6)
    g.add_undirected_edge(vertex_2, vertex_18, 2.3)
    g.add_undirected_edge(vertex_2, vertex_19, 6.0)
    g.add_undirected_edge(vertex_2, vertex_20, 7.8)
    g.add_undirected_edge(vertex_2, vertex_21, 4.3)
    g.add_undirected_edge(vertex_2, vertex_22, 4.8)
    g.add_undirected_edge(vertex_2, vertex_23, 6.3)
    g.add_undirected_edge(vertex_2, vertex_24, 1.1)
    g.add_undirected_edge(vertex_2, vertex_25, 4.0)
    g.add_undirected_edge(vertex_2, vertex_26, 9.3)
    g.add_undirected_edge(vertex_3, vertex_3, 0)
    g.add_undirected_edge(vertex_3, vertex_4, 5.4)
    g.add_undirected_edge(vertex_3, vertex_5, 1.0)
    g.add_undirected_edge(vertex_3, vertex_6, 7.6)
    g.add_undirected_edge(vertex_3, vertex_7, 5.3)
    g.add_undirected_edge(vertex_3, vertex_8, 0.6)
    g.add_undirected_edge(vertex_3, vertex_9, 2.8)
    g.add_undirected_edge(vertex_3, vertex_10, 11.9)
    g.add_undirected_edge(vertex_3, vertex_11, 7.2)
    g.add_undirected_edge(vertex_3, vertex_12, 4.2)
    g.add_undirected_edge(vertex_3, vertex_13, 8.5)
    g.add_undirected_edge(vertex_3, vertex_14, 10.3)
    g.add_undirected_edge(vertex_3, vertex_15, 7.8)
    g.add_undirected_edge(vertex_3, vertex_16, 11.1)
    g.add_undirected_edge(vertex_3, vertex_17, 7.5)
    g.add_undirected_edge(vertex_3, vertex_18, 5.9)
    g.add_undirected_edge(vertex_3, vertex_19, 14.1)
    g.add_undirected_edge(vertex_3, vertex_20, 11.5)
    g.add_undirected_edge(vertex_3, vertex_21, 7.8)
    g.add_undirected_edge(vertex_3, vertex_22, 9.5)
    g.add_undirected_edge(vertex_3, vertex_23, 4.8)
    g.add_undirected_edge(vertex_3, vertex_24, 4.7)
    g.add_undirected_edge(vertex_3, vertex_25, 6.6)
    g.add_undirected_edge(vertex_3, vertex_26, 7.7)
    g.add_undirected_edge(vertex_4, vertex_4, 0)
    g.add_undirected_edge(vertex_4, vertex_5, 4.4)
    g.add_undirected_edge(vertex_4, vertex_6, 3.0)
    g.add_undirected_edge(vertex_4, vertex_7, 3.6)
    g.add_undirected_edge(vertex_4, vertex_8, 5.4)
    g.add_undirected_edge(vertex_4, vertex_9, 4.3)
    g.add_undirected_edge(vertex_4, vertex_10, 6.9)
    g.add_undirected_edge(vertex_4, vertex_11, 6.1)
    g.add_undirected_edge(vertex_4, vertex_12, 6.7)
    g.add_undirected_edge(vertex_4, vertex_13, 4.6)
    g.add_undirected_edge(vertex_4, vertex_14, 6.6)
    g.add_undirected_edge(vertex_4, vertex_15, 2.2)
    g.add_undirected_edge(vertex_4, vertex_16, 6.0)
    g.add_undirected_edge(vertex_4, vertex_17, 1.7)
    g.add_undirected_edge(vertex_4, vertex_18, 1.6)
    g.add_undirected_edge(vertex_4, vertex_19, 6.9)
    g.add_undirected_edge(vertex_4, vertex_20, 6.5)
    g.add_undirected_edge(vertex_4, vertex_21, 3.9)
    g.add_undirected_edge(vertex_4, vertex_22, 5.6)
    g.add_undirected_edge(vertex_4, vertex_23, 5.0)
    g.add_undirected_edge(vertex_4, vertex_24, 1.0)
    g.add_undirected_edge(vertex_4, vertex_25, 1.7)
    g.add_undirected_edge(vertex_4, vertex_26, 4.6)
    g.add_undirected_edge(vertex_5, vertex_5, 0)
    g.add_undirected_edge(vertex_5, vertex_6, 6.9)
    g.add_undirected_edge(vertex_5, vertex_7, 4.3)
    g.add_undirected_edge(vertex_5, vertex_8, 1.0)
    g.add_undirected_edge(vertex_5, vertex_9, 1.8)
    g.add_undirected_edge(vertex_5, vertex_10, 11.5)
    g.add_undirected_edge(vertex_5, vertex_11, 7.2)
    g.add_undirected_edge(vertex_5, vertex_12, 3.2)
    g.add_undirected_edge(vertex_5, vertex_13, 7.5)
    g.add_undirected_edge(vertex_5, vertex_14, 9.3)
    g.add_undirected_edge(vertex_5, vertex_15, 6.8)
    g.add_undirected_edge(vertex_5, vertex_16, 10.6)
    g.add_undirected_edge(vertex_5, vertex_17, 6.5)
    g.add_undirected_edge(vertex_5, vertex_18, 4.9)
    g.add_undirected_edge(vertex_5, vertex_19, 13.1)
    g.add_undirected_edge(vertex_5, vertex_20, 11.4)
    g.add_undirected_edge(vertex_5, vertex_21, 6.8)
    g.add_undirected_edge(vertex_5, vertex_22, 8.5)
    g.add_undirected_edge(vertex_5, vertex_23, 4.8)
    g.add_undirected_edge(vertex_5, vertex_24, 3.7)
    g.add_undirected_edge(vertex_5, vertex_25, 6.4)
    g.add_undirected_edge(vertex_5, vertex_26, 6.7)
    g.add_undirected_edge(vertex_6, vertex_6, 0)
    g.add_undirected_edge(vertex_6, vertex_7, 6.5)
    g.add_undirected_edge(vertex_6, vertex_8, 7.3)
    g.add_undirected_edge(vertex_6, vertex_9, 6.4)
    g.add_undirected_edge(vertex_6, vertex_10, 4.9)
    g.add_undirected_edge(vertex_6, vertex_11, 4.0)
    g.add_undirected_edge(vertex_6, vertex_12, 4.2)
    g.add_undirected_edge(vertex_6, vertex_13, 6.2)
    g.add_undirected_edge(vertex_6, vertex_14, 8.2)
    g.add_undirected_edge(vertex_6, vertex_15, 1.3)
    g.add_undirected_edge(vertex_6, vertex_16, 3.9)
    g.add_undirected_edge(vertex_6, vertex_17, 3.2)
    g.add_undirected_edge(vertex_6, vertex_18, 3.2)
    g.add_undirected_edge(vertex_6, vertex_19, 10.5)
    g.add_undirected_edge(vertex_6, vertex_20, 4.4)
    g.add_undirected_edge(vertex_6, vertex_21, 5.5)
    g.add_undirected_edge(vertex_6, vertex_22, 7.2)
    g.add_undirected_edge(vertex_6, vertex_23, 3.0)
    g.add_undirected_edge(vertex_6, vertex_24, 3.5)
    g.add_undirected_edge(vertex_6, vertex_25, 1.5)
    g.add_undirected_edge(vertex_6, vertex_26, 1.6)
    g.add_undirected_edge(vertex_7, vertex_7, 0)
    g.add_undirected_edge(vertex_7, vertex_8, 5.3)
    g.add_undirected_edge(vertex_7, vertex_9, 2.8)
    g.add_undirected_edge(vertex_7, vertex_10, 10.4)
    g.add_undirected_edge(vertex_7, vertex_11, 5.7)
    g.add_undirected_edge(vertex_7, vertex_12, 8.6)
    g.add_undirected_edge(vertex_7, vertex_13, 3.3)
    g.add_undirected_edge(vertex_7, vertex_14, 5.0)
    g.add_undirected_edge(vertex_7, vertex_15, 5.6)
    g.add_undirected_edge(vertex_7, vertex_16, 9.2)
    g.add_undirected_edge(vertex_7, vertex_17, 4.4)
    g.add_undirected_edge(vertex_7, vertex_18, 4.1)
    g.add_undirected_edge(vertex_7, vertex_19, 7.4)
    g.add_undirected_edge(vertex_7, vertex_20, 9.7)
    g.add_undirected_edge(vertex_7, vertex_21, 6.1)
    g.add_undirected_edge(vertex_7, vertex_22, 6.1)
    g.add_undirected_edge(vertex_7, vertex_23, 7.1)
    g.add_undirected_edge(vertex_7, vertex_24, 3.0)
    g.add_undirected_edge(vertex_7, vertex_25, 5.8)
    g.add_undirected_edge(vertex_7, vertex_26, 6.3)
    g.add_undirected_edge(vertex_8, vertex_8, 0)
    g.add_undirected_edge(vertex_8, vertex_9, 2.8)
    g.add_undirected_edge(vertex_8, vertex_10, 12.0)
    g.add_undirected_edge(vertex_8, vertex_11, 7.2)
    g.add_undirected_edge(vertex_8, vertex_12, 4.2)
    g.add_undirected_edge(vertex_8, vertex_13, 8.5)
    g.add_undirected_edge(vertex_8, vertex_14, 10.3)
    g.add_undirected_edge(vertex_8, vertex_15, 7.8)
    g.add_undirected_edge(vertex_8, vertex_16, 11.1)
    g.add_undirected_edge(vertex_8, vertex_17, 7.5)
    g.add_undirected_edge(vertex_8, vertex_18, 5.9)
    g.add_undirected_edge(vertex_8, vertex_19, 14.1)
    g.add_undirected_edge(vertex_8, vertex_20, 11.5)
    g.add_undirected_edge(vertex_8, vertex_21, 7.8)
    g.add_undirected_edge(vertex_8, vertex_22, 9.5)
    g.add_undirected_edge(vertex_8, vertex_23, 4.8)
    g.add_undirected_edge(vertex_8, vertex_24, 4.7)
    g.add_undirected_edge(vertex_8, vertex_25, 6.6)
    g.add_undirected_edge(vertex_8, vertex_26, 7.7)
    g.add_undirected_edge(vertex_9, vertex_9, 0)
    g.add_undirected_edge(vertex_9, vertex_10, 11)
    g.add_undirected_edge(vertex_9, vertex_11, 6.2)
    g.add_undirected_edge(vertex_9, vertex_12, 5.1)
    g.add_undirected_edge(vertex_9, vertex_13, 6.0)
    g.add_undirected_edge(vertex_9, vertex_14, 7.9)
    g.add_undirected_edge(vertex_9, vertex_15, 6.5)
    g.add_undirected_edge(vertex_9, vertex_16, 10.1)
    g.add_undirected_edge(vertex_9, vertex_17, 5.4)
    g.add_undirected_edge(vertex_9, vertex_18, 5.1)
    g.add_undirected_edge(vertex_9, vertex_19, 8.3)
    g.add_undirected_edge(vertex_9, vertex_20, 10.6)
    g.add_undirected_edge(vertex_9, vertex_21, 6.8)
    g.add_undirected_edge(vertex_9, vertex_22, 7.0)
    g.add_undirected_edge(vertex_9, vertex_23, 4.4)
    g.add_undirected_edge(vertex_9, vertex_24, 3.7)
    g.add_undirected_edge(vertex_9, vertex_25, 5.7)
    g.add_undirected_edge(vertex_9, vertex_26, 6.2)
    g.add_undirected_edge(vertex_10, vertex_10, 0)
    g.add_undirected_edge(vertex_10, vertex_11, 8.1)
    g.add_undirected_edge(vertex_10, vertex_12, 8.6)
    g.add_undirected_edge(vertex_10, vertex_13, 6.9)
    g.add_undirected_edge(vertex_10, vertex_14, 8.3)
    g.add_undirected_edge(vertex_10, vertex_15, 5.2)
    g.add_undirected_edge(vertex_10, vertex_16, 1.0)
    g.add_undirected_edge(vertex_10, vertex_17, 6.5)
    g.add_undirected_edge(vertex_10, vertex_18, 6.2)
    g.add_undirected_edge(vertex_10, vertex_19, 6.8)
    g.add_undirected_edge(vertex_10, vertex_20, 0.4)
    g.add_undirected_edge(vertex_10, vertex_21, 4.1)
    g.add_undirected_edge(vertex_10, vertex_22, 4.9)
    g.add_undirected_edge(vertex_10, vertex_23, 7.3)
    g.add_undirected_edge(vertex_10, vertex_24, 7.3)
    g.add_undirected_edge(vertex_10, vertex_25, 5.4)
    g.add_undirected_edge(vertex_10, vertex_26, 4.6)
    g.add_undirected_edge(vertex_11, vertex_11, 0)
    g.add_undirected_edge(vertex_11, vertex_12, 7.2)
    g.add_undirected_edge(vertex_11, vertex_13, 10.6)
    g.add_undirected_edge(vertex_11, vertex_14, 12.0)
    g.add_undirected_edge(vertex_11, vertex_15, 6.4)
    g.add_undirected_edge(vertex_11, vertex_16, 7.2)
    g.add_undirected_edge(vertex_11, vertex_17, 1.4)
    g.add_undirected_edge(vertex_11, vertex_18, 7.1)
    g.add_undirected_edge(vertex_11, vertex_19, 13.6)
    g.add_undirected_edge(vertex_11, vertex_20, 7.5)
    g.add_undirected_edge(vertex_11, vertex_21, 9.4)
    g.add_undirected_edge(vertex_11, vertex_22, 11.1)
    g.add_undirected_edge(vertex_11, vertex_23, 7.4)
    g.add_undirected_edge(vertex_11, vertex_24, 6.3)
    g.add_undirected_edge(vertex_11, vertex_25, 5.6)
    g.add_undirected_edge(vertex_11, vertex_26, 3.1)
    g.add_undirected_edge(vertex_12, vertex_12, 0)
    g.add_undirected_edge(vertex_12, vertex_13, 11.2)
    g.add_undirected_edge(vertex_12, vertex_14, 12.7)
    g.add_undirected_edge(vertex_12, vertex_15, 8.0)
    g.add_undirected_edge(vertex_12, vertex_16, 8.6)
    g.add_undirected_edge(vertex_12, vertex_17, 7.9)
    g.add_undirected_edge(vertex_12, vertex_18, 7.7)
    g.add_undirected_edge(vertex_12, vertex_19, 14.2)
    g.add_undirected_edge(vertex_12, vertex_20, 8.2)
    g.add_undirected_edge(vertex_12, vertex_21, 10.0)
    g.add_undirected_edge(vertex_12, vertex_22, 11.7)
    g.add_undirected_edge(vertex_12, vertex_23, 1.6)
    g.add_undirected_edge(vertex_12, vertex_24, 6.9)
    g.add_undirected_edge(vertex_12, vertex_25, 5.8)
    g.add_undirected_edge(vertex_12, vertex_26, 4.0)
    g.add_undirected_edge(vertex_13, vertex_13, 0)
    g.add_undirected_edge(vertex_13, vertex_14, 2.0)
    g.add_undirected_edge(vertex_13, vertex_15, 5.3)
    g.add_undirected_edge(vertex_13, vertex_16, 5.9)
    g.add_undirected_edge(vertex_13, vertex_17, 3.2)
    g.add_undirected_edge(vertex_13, vertex_18, 3.0)
    g.add_undirected_edge(vertex_13, vertex_19, 4.1)
    g.add_undirected_edge(vertex_13, vertex_20, 6.4)
    g.add_undirected_edge(vertex_13, vertex_21, 2.9)
    g.add_undirected_edge(vertex_13, vertex_22, 2.8)
    g.add_undirected_edge(vertex_13, vertex_23, 9.5)
    g.add_undirected_edge(vertex_13, vertex_24, 4.1)
    g.add_undirected_edge(vertex_13, vertex_25, 4.9)
    g.add_undirected_edge(vertex_13, vertex_26, 8.1)
    g.add_undirected_edge(vertex_14, vertex_14, 0)
    g.add_undirected_edge(vertex_14, vertex_15, 7.4)
    g.add_undirected_edge(vertex_14, vertex_16, 7.4)
    g.add_undirected_edge(vertex_14, vertex_17, 5.2)
    g.add_undirected_edge(vertex_14, vertex_18, 5.0)
    g.add_undirected_edge(vertex_14, vertex_19, 4.7)
    g.add_undirected_edge(vertex_14, vertex_20, 7.9)
    g.add_undirected_edge(vertex_14, vertex_21, 4.4)
    g.add_undirected_edge(vertex_14, vertex_22, 3.4)
    g.add_undirected_edge(vertex_14, vertex_23, 10.9)
    g.add_undirected_edge(vertex_14, vertex_24, 6.2)
    g.add_undirected_edge(vertex_14, vertex_25, 6.9)
    g.add_undirected_edge(vertex_14, vertex_26, 10.4)
    g.add_undirected_edge(vertex_15, vertex_15, 0)
    g.add_undirected_edge(vertex_15, vertex_16, 4.3)
    g.add_undirected_edge(vertex_15, vertex_17, 2.4)
    g.add_undirected_edge(vertex_15, vertex_18, 2.4)
    g.add_undirected_edge(vertex_15, vertex_19, 8.8)
    g.add_undirected_edge(vertex_15, vertex_20, 4.8)
    g.add_undirected_edge(vertex_15, vertex_21, 4.6)
    g.add_undirected_edge(vertex_15, vertex_22, 6.3)
    g.add_undirected_edge(vertex_15, vertex_23, 4.6)
    g.add_undirected_edge(vertex_15, vertex_24, 2.3)
    g.add_undirected_edge(vertex_15, vertex_25, 0.6)
    g.add_undirected_edge(vertex_15, vertex_26, 3.3)
    g.add_undirected_edge(vertex_16, vertex_16, 0)
    g.add_undirected_edge(vertex_16, vertex_17, 5.6)
    g.add_undirected_edge(vertex_16, vertex_18, 5.3)
    g.add_undirected_edge(vertex_16, vertex_19, 10.1)
    g.add_undirected_edge(vertex_16, vertex_20, 0.6)
    g.add_undirected_edge(vertex_16, vertex_21, 4.7)
    g.add_undirected_edge(vertex_16, vertex_22, 6.4)
    g.add_undirected_edge(vertex_16, vertex_23, 6.4)
    g.add_undirected_edge(vertex_16, vertex_24, 6.4)
    g.add_undirected_edge(vertex_16, vertex_25, 4.4)
    g.add_undirected_edge(vertex_16, vertex_26, 4.0)
    g.add_undirected_edge(vertex_17, vertex_17, 0)
    g.add_undirected_edge(vertex_17, vertex_18, 0.5)
    g.add_undirected_edge(vertex_17, vertex_19, 5.5)
    g.add_undirected_edge(vertex_17, vertex_20, 6.0)
    g.add_undirected_edge(vertex_17, vertex_21, 2.5)
    g.add_undirected_edge(vertex_17, vertex_22, 4.2)
    g.add_undirected_edge(vertex_17, vertex_23, 6.0)
    g.add_undirected_edge(vertex_17, vertex_24, 1.5)
    g.add_undirected_edge(vertex_17, vertex_25, 2.7)
    g.add_undirected_edge(vertex_17, vertex_26, 5.1)
    g.add_undirected_edge(vertex_18, vertex_18, 0)
    g.add_undirected_edge(vertex_18, vertex_19, 5.2)
    g.add_undirected_edge(vertex_18, vertex_20, 5.5)
    g.add_undirected_edge(vertex_18, vertex_21, 2.3)
    g.add_undirected_edge(vertex_18, vertex_22, 4.0)
    g.add_undirected_edge(vertex_18, vertex_23, 6.0)
    g.add_undirected_edge(vertex_18, vertex_24, 1.2)
    g.add_undirected_edge(vertex_18, vertex_25, 1.6)
    g.add_undirected_edge(vertex_18, vertex_26, 5.1)
    g.add_undirected_edge(vertex_19, vertex_19, 0)
    g.add_undirected_edge(vertex_19, vertex_20, 7.8)
    g.add_undirected_edge(vertex_19, vertex_21, 3.1)
    g.add_undirected_edge(vertex_19, vertex_22, 1.3)
    g.add_undirected_edge(vertex_19, vertex_23, 13.0)
    g.add_undirected_edge(vertex_19, vertex_24, 6.4)
    g.add_undirected_edge(vertex_19, vertex_25, 8.4)
    g.add_undirected_edge(vertex_19, vertex_26, 10.7)
    g.add_undirected_edge(vertex_20, vertex_20, 0)
    g.add_undirected_edge(vertex_20, vertex_21, 4.5)
    g.add_undirected_edge(vertex_20, vertex_22, 5.4)
    g.add_undirected_edge(vertex_20, vertex_23, 6.9)
    g.add_undirected_edge(vertex_20, vertex_24, 6.9)
    g.add_undirected_edge(vertex_20, vertex_25, 5.6)
    g.add_undirected_edge(vertex_20, vertex_26, 4.2)
    g.add_undirected_edge(vertex_21, vertex_21, 0)
    g.add_undirected_edge(vertex_21, vertex_22, 1.7)
    g.add_undirected_edge(vertex_21, vertex_23, 8.3)
    g.add_undirected_edge(vertex_21, vertex_24, 3.4)
    g.add_undirected_edge(vertex_21, vertex_25, 4.2)
    g.add_undirected_edge(vertex_21, vertex_26, 7.8)
    g.add_undirected_edge(vertex_22, vertex_22, 0)
    g.add_undirected_edge(vertex_22, vertex_23, 10.0)
    g.add_undirected_edge(vertex_22, vertex_24, 24.0)
    g.add_undirected_edge(vertex_22, vertex_25, 5.9)
    g.add_undirected_edge(vertex_22, vertex_26, 9.5)
    g.add_undirected_edge(vertex_23, vertex_23, 0)
    g.add_undirected_edge(vertex_23, vertex_24, 5.3)
    g.add_undirected_edge(vertex_23, vertex_25, 4.5)
    g.add_undirected_edge(vertex_23, vertex_26, 2.8)
    g.add_undirected_edge(vertex_24, vertex_24, 0)
    g.add_undirected_edge(vertex_24, vertex_25, 2.9)
    g.add_undirected_edge(vertex_24, vertex_26, 4.8)
    g.add_undirected_edge(vertex_25, vertex_25, 0)
    g.add_undirected_edge(vertex_25, vertex_26, 3.4)
    g.add_undirected_edge(vertex_26, vertex_26, 0)


creategraph()  # Function call to populate graph g.


# Function to get the distance between 2 vertex.
def getdistance(Vetrex1, Vertex2):
    edge_weight = g.edge_weights[(Vetrex1, Vertex2)]
    return float(edge_weight)


# Timer to track total time elapsed, accepts miles traveled.
def totaltimer(miles):
    timer = int(miles / 0.3)
    newhour = (8 + (timer // 60))
    newminute = timer % 60

    if newhour > 12:
        newhour = newhour - 12

    print("Time ", newhour, ":", '%0.2d' % newminute)


# Returns timer in minutes, accepts miles traveled.
def gettotaltimer(miles):
    timer = int(miles / 0.3)
    return timer


# Returns hour, accepts miles.
def gettotlalhour(miles):
    timer = int(miles / 0.3)
    newhour = (8 + (timer // 60))
    # newminute = (timer % 60)

    if newhour > 12:
        newhour = newhour - 12

    return newhour


# Returns minutes, accepts miles.
def gettotalminute(miles):
    timer = int(miles / 0.3)
    # newhour = (timer // 60)
    newminute = (timer % 60)

    # if newhour > 12:
    # newhour = newhour - 12

    return newminute


# Returns hour, accepts departure hour and minute.
def gethour(dhour, dminute, miles):
    timer = int(miles / 0.3)
    newhour = (dhour + ((timer - dminute) // 60))
    newminute = ((timer - dminute) % 60)

    if newhour > 12:
        newhour = newhour - 12

    return newhour


# Returns minute, accepts departure hour and minute.
def getminute(dhour, dminute, miles):
    timer = int(miles / 0.3)
    newhour = (dhour + ((timer - dminute) // 60))
    newminute = ((timer - dminute) % 60)

    if newhour > 12:
        newhour = newhour - 12

    return newminute


# Prints myhashtable package status base on time, accepts hour and minute.
def getstatusbytime(hour, minute):
    statusnow = "at HUB until"
    printhour = hour
    if hour < 8:
        hour = hour + 12
    for i in range(40):
        p = importcsv.myHash.search(i+1)
        dhour = int(float(p.deliveredhour))
        dminute = int(float(p.deliveredminute))



        if (dhour < hour or (dhour == hour and dminute <= minute)):
            print("Package ID ", p.id, p.trucknum,"Address ", p.address, " Delivered at", p.deliveredhour, ":", '%0.2d' % p.deliveredminute)
        elif (p.loadtime[0] > hour or (p.loadtime[0] == hour and p.loadtime[1] > minute)):
            print("Package ID ", p.id, p.trucknum, "Address ", p.address, statusnow, p.loadtime[0], ":", '%0.2d' % p.loadtime[1])
        else:
            print("Package ID ", p.id, p.trucknum, "Address ", p.address, " Enroute at ", printhour, ":",  '%0.2d' % minute)



t1undelivered = []  # List to hold packages on truck 1.
t2undelivered = []  # List to hold packages on truck 2.
t3undelivered = []  # List to hold packages on truck 3.
deliveredpackages = []  # List to store all delivered packages.

truck1 = Truck("Truck 1", 8, 00, "HUB", 8, 15, t1undelivered, 0)  # Instantiate Truck 1.
truck2 = Truck("Truck 2", 9, 5, "HUB", 8, 15, t2undelivered, 0)  # Instantiate Truck 2.
truck3 = Truck("Truck 3", 10, 20, "HUB", 8, 15, t3undelivered, 0)  # Instantiate Truck 3.


# Function to populate the package list for each truck.
def loadtrucks():
    # Load truck 1

    # t1undelivered.append(0)
    t1undelivered.append(4)
    t1undelivered.append(13)
    t1undelivered.append(29)
    t1undelivered.append(14)
    t1undelivered.append(15)
    t1undelivered.append(16)
    t1undelivered.append(17)
    t1undelivered.append(19)
    t1undelivered.append(20)
    t1undelivered.append(21)
    t1undelivered.append(28)
    t1undelivered.append(31)
    t1undelivered.append(32)
    t1undelivered.append(34)
    t1undelivered.append(1)
    t1undelivered.append(40)

    for i in range(len(t1undelivered)):
        p = importcsv.myHash.search(t1undelivered[i])
        p.trucknum = truck1.trucknumber
        p.loadtime = []
        p.loadtime.append(8)
        p.loadtime.append(00)
    # Load truck 2

    # t2undelivered.append(0)
    t2undelivered.append(37)
    t2undelivered.append(30)
    t2undelivered.append(25)
    t2undelivered.append(38)
    t2undelivered.append(3)
    t2undelivered.append(5)
    t2undelivered.append(6)
    t2undelivered.append(8)
    t2undelivered.append(10)
    t2undelivered.append(11)
    t2undelivered.append(12)
    t2undelivered.append(18)
    t2undelivered.append(23)
    t2undelivered.append(26)
    t2undelivered.append(36)

    for i in range(len(t2undelivered)):
        p = importcsv.myHash.search(t2undelivered[i])
        p.trucknum = truck2.trucknumber
        p.loadtime = []
        p.loadtime.append(9)
        p.loadtime.append(0o05)

    # Load truck 3

    # t3undelivered.append(0)
    t3undelivered.append(2)
    t3undelivered.append(7)
    t3undelivered.append(9)
    t3undelivered.append(22)
    t3undelivered.append(24)
    t3undelivered.append(27)
    t3undelivered.append(33)
    t3undelivered.append(35)
    t3undelivered.append(39)

    for i in range(len(t3undelivered)):
        p = importcsv.myHash.search(t3undelivered[i])
        p.trucknum = truck3.trucknumber
        p.loadtime = []
        p.loadtime.append(10)
        p.loadtime.append(20)


loadtrucks()  # Function call to load trucks.

distanceTraveled: float = 0.0  # Define variable to carry total distance traveled.


# Function to sort and deliver the packages on truck 1.
def t1deliver():
    global distanceTraveled
    ordered = []
    orderedweights = []
    currentvertex = 0
    tempvertex = 0
    tempweight = 0
    temppackage = 0

    for i in range(len(t1undelivered)):
        t = importcsv.myHash.search(t1undelivered[i])
        nextlocationweight = getdistance(currentvertex, t.vertex)
        for j in range(len(t1undelivered)):
            p = importcsv.myHash.search(t1undelivered[j])
            if p.vertex in ordered:
                pass
            elif getdistance(currentvertex, p.vertex) <= nextlocationweight and p.vertex not in ordered:
                tempvertex = p.vertex
                tempweight = getdistance(currentvertex, p.vertex)
                temppackage = t1undelivered[j]

        ordered.append(currentvertex)
        currentvertex = tempvertex
        distanceTraveled = distanceTraveled + tempweight
        truck1.miles = truck1.miles + tempweight

        p = importcsv.myHash.search(t1undelivered[i])
        truck1.location = p.address
        p.deliveredhour = gettotlalhour(distanceTraveled)
        p.deliveredminute = gettotalminute(distanceTraveled)
        p.status = " Delivered "
        p.weight = 1

        deliveredpackages.append(p)
    distanceTraveled = distanceTraveled + getdistance(currentvertex, 0)


# Function to sort and deliver the packages on truck 2.
def t2deliver():
    global distanceTraveled
    truck2distance = 0
    ordered = []
    orderedweights = []
    currentvertex = 0
    tempvertex = 0
    tempweight = 0
    temppackage = []
    for i in range(len(t2undelivered)):

        t = importcsv.myHash.search(t2undelivered[i])

        # print(t.vertex)
        # print(currentvertex)
        nextlocationweight = getdistance(currentvertex, t.vertex)
        for j in range(len(t2undelivered)):
            p = importcsv.myHash.search(t2undelivered[j])
            if p.vertex in ordered:
                pass
            elif p.deadlineindicator == '0':
                tempvertex = p.vertex
                tempweight = getdistance(currentvertex, p.vertex)

            elif getdistance(currentvertex, p.vertex) <= nextlocationweight and p.vertex not in ordered:
                tempvertex = p.vertex
                tempweight = getdistance(currentvertex, p.vertex)
        p = importcsv.myHash.search(t2undelivered[i])
        temppackage.append(tempweight)
        ordered.append(currentvertex)
        orderedweights.append(tempweight)
        currentvertex = tempvertex
        distanceTraveled = distanceTraveled + tempweight
        truck2.miles = truck2.miles + tempweight
        truck2distance = truck2distance + tempweight
        p.deliveredhour = gettotlalhour(distanceTraveled)
        p.deliveredminute = gettotalminute(distanceTraveled)
        p = importcsv.myHash.search(t2undelivered[i])
        p.status = " Delivered "
        p.weight = 2

        deliveredpackages.append(p)
    distanceTraveled = distanceTraveled + getdistance(currentvertex, 0)


# Function to sort and deliver the packages on truck 3.
def t3deliver():
    global distanceTraveled
    ordered = []
    orderedweights = []
    truck3distance = 0
    currentvertex = 0
    tempvertex = 0
    tempweight = 0
    temppackage = 0
    for i in range(len(t3undelivered)):

        if t3undelivered[i] == 9:
            importcsv.myHash.search(t3undelivered[i]).address = "410 S State St"
            importcsv.myHash.search(t3undelivered[i]).trucknum = truck3.trucknumber

            #print(importcsv.myHash.search(t3undelivered[i]).address)
        t = importcsv.myHash.search(t3undelivered[i])
        nextlocationweight = getdistance(currentvertex, t.vertex)
        for j in range(len(t3undelivered) - 1):
            p = importcsv.myHash.search(t3undelivered[j])
            if p.vertex in ordered:
                pass
            elif getdistance(currentvertex, p.vertex) <= nextlocationweight and p.vertex not in ordered:
                tempvertex = p.vertex
                tempweight = getdistance(currentvertex, p.vertex)
                temppackage = t3undelivered[j]

        ordered.append(currentvertex)
        currentvertex = tempvertex
        distanceTraveled = distanceTraveled + tempweight
        truck3.miles = truck3.miles + tempweight
        truck3distance = truck3distance + tempweight
        p = importcsv.myHash.search(t3undelivered[i])
        truck3.location = p.address
        p.deliveredhour = gettotlalhour(distanceTraveled)
        p.deliveredminute = gettotalminute(distanceTraveled)
        p.status = " Delivered "
        p.weight = 3
        # print("Truck 3 Package number: ", t3undelivered[i], " Address: ", p.address, " Delivery deadline ", p.deadline,
        #       "delivered at:", gethour(truck3.dhour, truck3.dminute, truck3distance), ":",
        #       '%0.2d' % getminute(truck3.dhour, truck3.dminute, truck3distance))
        deliveredpackages.append(p)
    distanceTraveled = distanceTraveled + getdistance(currentvertex, 0)


# User interface function.
def userinterface():
    count = 0

    while count < 10:
        print("\n")
        print("Enter 3 to return all packages")
        print("Enter 2 to search by Package id.")
        print("Enter 1 to search by time.(Enter hour and then minute when prompted.)")
        print("Enter 0 to exit.")

        val = input()

        if val == '0':
            return

        if val == '1':
            print("Enter hour.")
            h = int(input())
            print("Enter minute.")
            m = int(input())

            getstatusbytime(h, m)

        if val == '2':
            print("Enter a package id.")
            id = input()
            p = importcsv.myHash.search(int(id))
            print("Package ID ", p.id, "Address ", p.address, " status ", p.status, p.trucknum, "Time loaded ", p.loadtime,
                      "delivered at:", p.deliveredhour, ":",
                      '%0.2d' % p.deliveredminute)

        if val == '3':
            for i in range(39):  # Print all packages
                p = importcsv.myHash.search(i + 1)
                print("Truck #", p.trucknum, "Package number: ", p.id, " Address: ", p.address, " Delivery deadline ",
                      p.deadline,
                      "delivered at:", p.deliveredhour, ":",
                      '%0.2d' % p.deliveredminute)



t1deliver()  # Function call to deliver the packages on truck 1.

t2deliver()  # Function call to deliver the packages on truck 2.

t3deliver()  # Function call to deliver the packages on truck 2.

for i in range(40):  # Print all packages
    p = importcsv.myHash.search(i + 1)
    print("Truck #", p.trucknum, "Package number: ", p.id, " Address: ", p.address, " Delivery deadline ", p.deadline,
          "delivered at:", p.deliveredhour, ":",
          '%0.2d' % p.deliveredminute)

print("\n", "Total distance traveled: ", str(round(distanceTraveled, 1)), "miles.")  # Print total distance traveled
print( truck1.trucknumber, "Distance traveled", truck1.miles, "miles.")
print( truck2.trucknumber, "Distance traveled", truck2.miles, "miles.")
print( truck3.trucknumber, "Distance traveled", truck3.miles, "miles.")

userinterface()  # Function call to run the user interface.


