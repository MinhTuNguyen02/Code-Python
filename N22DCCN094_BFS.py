from collections import deque

class Problem:
    def __init__(self, graph, start, end):
        self.graph = graph
        self.start = start
        self.end = end
    
    def goal_test(self, state):
        if state == self.end:
            return True
        return False
    
    def Actions(self, state):
        a=[]
        for i in graph[state]:
            a.append(i) 
        return a
    
    def Result(selt,state,action):
        return graph[state][action]
    
class Node:
    def __init__(self, state, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action

def child_node(problem,parent,action):
    node = Node(state= problem.Result(parent.state,action), parent=parent, action=action)
    return node

def Solution(node):
    path=[]
    while 1:
        path.insert(0,node.state)
        if node.parent==None: break
        node=node.parent
    print("Solution:",end=" ")
    print(*path,sep=' -> ')


def bfs(problem):
    root_node = Node(problem.start)
    frontier = deque([root_node]) 
    explored = set()
    print(f"Frontier: {[node.state for node in frontier]}")
    print(f"Explored: []")
    
    
    while frontier:
        current_node = frontier.popleft()
        explored.add(current_node.state)
        if problem.goal_test(current_node.state):
            return Solution(current_node)

        for action in range(problem.Actions(current_node.state).__len__()):
            child = child_node(problem,current_node,action)
            f=True        
            for i in frontier:
                if i.state==child.state: f=False
            if child.state not in explored and f:              
                    frontier.append(child)
        print(f"Frontier: {[node.state for node in frontier]}")
        print(f"Explored: {explored}")

graph = {
    "Arab": ["Zerind", "Sibiu", "Timisoara"],
    "Zerind": ["Oradea", "Arab"],
    "Oradea": ["Sibiu", "Zerind"],
    "Sibiu": ["Fagaras", "Rimnicu Vilcea", "Oradea", "Arab"],
    "Fagaras": ["Bucharest", "Sibiu"],
    "Rimnicu Vilcea": ["Craiova", "Pitesti", "Sibiu"],
    "Craiova": ["Pitesti", "Rimnicu Vilcea"],
    "Pitesti": ["Bucharest", "Rimnicu Vilcea", "Craiova"],
    "Timisoara": ["Lugoj", "Arab"],
    "Lugoj": ["Mehadia", "Timisoara"],
    "Mehadia": ["Drobeta", "Lugoj"],
    "Drobeta": ["Craiova", "Mehadia"],
    "Bucharest": ["Fagaras", "Pitesti", "Giurgiu", "Urziceni"],
    "Giurgiu": ["Bucharest"],
    "Urziceni": ["Bucharest", "Hirsova", "Vaslui"],
    "Hirsova": ["Eforie", "Urziceni"],
    "Eforie": ["Hirsova"],
    "Vaslui": ["Iasi", "Urziceni"],
    "Iasi": ["Neamt", "Vaslui"],
    "Neamt": ["Iasi"]
}

start = "Arab"
end = "Bucharest"

problem = Problem(graph,start,end)
bfs(problem)