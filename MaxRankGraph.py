import heapq

def solution1(A, B, n):

    nodes = {}

    for node in range(n):
        nodes[node+1] = []

    for city1, city2 in zip(A,B):
        nodes[city1].append(city2)
        nodes[city2].append(city1)

    paths = {}


    for city1, city2 in zip(A, B):
        if (city1, city2) not in paths:
            paths[(city1, city2)] = []

        for p in nodes[city1]:
            paths[(city1, city2)].append((city1, p))


        for p in nodes[city2]:
            paths[(city1, city2)].append((city2, p))


    print (paths)
    max = -1

    for p in paths:
        if len(paths[p]) > max:
            max = len(paths[p])

    return max - 1




def solution2(A, B, n):

    nodes = {}

# init graph
    for city1, city2 in zip(A,B):

        if city1 not in nodes:
            nodes[city1] = []

        if city2 not in nodes:
            nodes[city2] = []


        nodes[city1].append(city2)
        nodes[city2].append(city1)

    paths = {}

# build paths graph
    for city1, city2 in zip(A, B):
        if (city1, city2) not in paths:
            paths[(city1, city2)] = []

        for p in nodes[city1]:
            paths[(city1, city2)].append((city1, p))

        for p in nodes[city2]:
            paths[(city1, city2)].append((city2, p))


    print (paths)

    max_heap = heapq.nlargest(1, paths, key=lambda s: len(paths[s]))

    if (len(max_heap) == 1):
        return (len(paths[max_heap[0]]) - 1)

    return (0)


def solution_pranav(A,B,N):

    edge_tuple = []

    i=j=0

    edge_dict={}

    while i<len(A):
        edge_tuple.append((A[i],B[j]))
        i=i+1
        j=j+1





    for item in edge_tuple:
        ct1=ct2=0
        for b in range(len(A)):
            if item[0] == A[b] or item[1]== B[b]:
                ct1=ct1+1
        for c in range(len(B)):
            if item[0] == A[c] or item[1]== B[c]:
                ct2=ct2+1


        edge_dict[item]=ct1+ct2
    #print edge_dict

    return max(edge_dict.values())

A = [1, 2, 3, 3]
B = [2, 3, 1, 4]

print (solution_pranav(A, B, 4))

A = [1, 2, 4, 5]
B = [2, 3, 5, 6]

print (solution_pranav(A, B, 6))