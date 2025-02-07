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


def make_node(start):
    node = Node(start)
    return node

def dls(problem, limit):
    return recursive_dls(make_node(problem.start),problem,limit)

visit=[]
def recursive_dls(node, problem, limit):
    print(node.state,'limit: {}'.format(limit),sep=' ')
    visit.append(node.state)
    if problem.goal_test(node.state):
        return Solution(node)
    elif limit==0:
        return "cutoff"
    else:
        cutoff_occurred = False
        for action in range(problem.Actions(node.state).__len__()):
            child=child_node(problem,node,action)
            if child.state in visit:
                continue
            result=recursive_dls(child,problem,limit-1)
            visit.pop(len(visit)-1)
            if result=='cutoff':
                cutoff_occurred=True
            elif result!='failure':
                return result
        
        if cutoff_occurred:
            return 'cutoff'
        else:
            return 'failure'



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
limit = 3

problem = Problem(graph,start,end)
print(dls(problem,limit))