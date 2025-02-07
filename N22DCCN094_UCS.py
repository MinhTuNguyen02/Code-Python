from collections import deque
import heapq

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
        return graph[state][action][0]
    
    def Step_cost(self, state, action):
        return self.graph[state][action][1]
    
class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost=path_cost

    def __lt__(self, other):
        return self.path_cost < other.path_cost

def child_node(problem,parent,action):
    node = Node(state= problem.Result(parent.state,action), 
                parent=parent, 
                action=action,
                path_cost=parent.path_cost+problem.Step_cost(parent.state,action))
    return node

def Solution(node):
    path=[]
    cost=node.path_cost
    while 1:
        path.insert(0,node.state)
        if node.parent==None: break
        node=node.parent
    print("Solution:",end=" ")
    print(*path,sep=' -> ')
    print('cost:',cost,sep=" ")
    


def ucs(problem):
    root_node = Node(problem.start)
    frontier = []  
    heapq.heappush(frontier, root_node)
    explored = set()
    print(f"Frontier: {[node.state for node in frontier]}")
    print(f"Explored: []")

    while frontier:
        current_node = heapq.heappop(frontier) 
        explored.add(current_node.state)
        if problem.goal_test(current_node.state):                            
            return Solution(current_node)

        for action in range(problem.Actions(current_node.state).__len__()):
            child = child_node(problem,current_node,action)
            f=True        
            for i in frontier:
                if i.state==child.state: f=False
            if child.state not in explored:
                if not any(c.state == problem.graph[current_node.state][action][0] and c.path_cost < child.path_cost for c in frontier):
                    print(child.path_cost)
                    heapq.heappush(frontier, child)
                                            
        print(f"Frontier: {[node.state for node in frontier]}")
        print(f"Explored: {explored}")

graph = {
    "Arab": [("Zerind",75), ("Sibiu",140), ("Timisoara",118)],
    "Zerind": [("Oradea",71), ("Arab",75)],
    "Oradea": [("Sibiu",151), ("Zerind",71)],
    "Sibiu": [("Fagaras",99), ("Rimnicu Vilcea",80), ("Oradea",151), ("Arab",140)],
    "Fagaras": [("Bucharest",211), ("Sibiu",99)],
    "Rimnicu Vilcea": [("Craiova",146), ("Pitesti",97), ("Sibiu",80)],
    "Craiova": [("Pitesti",138), ("Rimnicu Vilcea",146), ("Drobeta",120)],
    "Pitesti": [("Bucharest",101), ("Rimnicu Vilcea",97), ("Craiova",138)],
    "Timisoara": [("Lugoj",111), ("Arab",118)],
    "Lugoj": [("Mehadia",70), ("Timisoara",111)],
    "Mehadia": [("Drobeta",75), ("Lugoj",70)],
    "Drobeta": [("Craiova",120), ("Mehadia",75)],
    "Bucharest": [("Fagaras",211), ("Pitesti",101), ("Giurgiu",90), ("Urziceni",85)],
    "Giurgiu": [("Bucharest",90)],
    "Urziceni": [("Bucharest",85), ("Hirsova",98), ("Vaslui",142)],
    "Hirsova": [("Eforie",86), ("Urziceni",98)],
    "Eforie": [("Hirsova",86)],
    "Vaslui": [("Iasi",92), ("Urziceni",142)],
    "Iasi": [("Neamt",87), ("Vaslui",92)],
    "Neamt": [("Iasi",87)]
}

start = "Arab"
end = "Bucharest"

problem = Problem(graph,start,end)
ucs(problem)


