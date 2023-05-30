graph = {
'A': ['B', 'C', "D"],
'B': ['E', "F"],
'C': ['G', "I"],
'D': ["I"],
'E': [],
"F": [],
'G': [],
"I": []
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
bfs([], graph, 'A')


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited
graph = {'0': set(['1', '2']),
'1': set(['0', '3', '4']),
'2': set(['0']),
'3': set(['1']),
'4': set(['2', '3'])}
dfs(graph, '0')