graph={
    "a":["b","c","d"] ,
    "b":["e","f"] ,
    "c":["g","h"] ,
    "d":["i"],
    "e":[],
    "f":[],
    "g":[],
    "h":[]
    }
def bfs(visit_complete, graph, current_node):
    visit_complete.append(current_node)
    queue = []
    queue.append(current_node)
 
    while queue:
        s = queue.pop(0)
        print(s)
 
        for neighbour in graph[s]:
            if neighbour not in visit_complete:
                visit_complete.append(neighbour)
                queue.append(neighbour)
 
bfs([], graph, 'a')

#DFS CODE:

def dfs(graph,start,visited=None):
    if visited is None:
        visited=set()
    visited.add(start)
    print(start)
    for next in graph[start]-visited:
        dfs(graph,next,visited)
    return visited
graph={'1':set(['1','2']) ,
       '2':set(['0','3','4']),
       '3':set(['1']),
       '4':set(['2','3'])
       }
dfs(graph,'1')

