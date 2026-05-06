import json
with open("C:\\Users\\Admin\\Downloads\\shortest_path_graph.json", "r") as read_file:
    graph = json.load(read_file)
print(graph)
places = {node["id"]: node["name"] for node in graph["nodes"]}
print(places)
print(graph["edges"])
paths = {edge["from"] + "->" + edge["to"]: edge["distance"] for edge in graph["edges"]}
print(paths)
'''
a = input()
b = input()
for i in places.items():
    if a == i[1]:
        loc_a = i[0]
    if b == i[1]:
        loc_b = i[0]
'''

n = []
for i in range(len(places)):
    n.append([])
    for j in range(len(places)):
        n[i].append(float("inf"))
print(n)

for i in paths.keys():
    n[ord(i[0])- 65][ord(i[3]) - 65] = paths[i[0] + "->" + i[3]]
    n[ord(i[3]) - 65][ord(i[0]) - 65] = paths[i[0] + "->" + i[3]]

for i in range(len(n)):
    n[i][i] = 0

for i in n:
    print(i)
print()


INF = float('inf')

'''
if n[i][j] != -1 and n[i+1][j+1] != -1:
    n[i+1][j] = min(n[i+1][j], n[i][j]+ n[i+1][j+1]) 
    n[j][i+1] = min(n[i + 1][j], n[i][j] + n[i + 1][j + 1])
'''

for k in range(len(n)):
    for i in range(len(n)):
        for j in range(len(n)):
            if n[i][k] != INF and n[k][j] != INF:
                new_val = n[i][k] + n[k][j]
                if new_val < n[i][j]:
                    n[i][j] = new_val
    for i in n:
        print(i)
    print()
#print (i for i in n)

for i in n:
    print(i)



