class Problem:
    def __init__(self, hn, graph, start, end):
        self.graph = graph
        self.hn=hn
        self.start = start
        self.end = end
    
    def goal_test(self, state):
        if state == self.end:
            return True
        return False
    
    def Actions(self, state):
        a=[]
        for i in graph[state]:
            a.append(i[0]) 
        return a
    
    def Result(selt,state,action):
        return graph[state][action][0]
    
    def Step_cost(self, state, action):
        return graph[state][action][1]

    
class Node:
    def __init__(self, state, h=None, path_cost=0,parent=None, action=None):
        self.state = state
        self.h=hn[state]
        self.path_cost=path_cost
        self.parent = parent
        self.action = action

    def __lt__(self, other):
        return (self.h + self.path_cost) < (other.h + other.path_cost)

def child_node(problem,parent,action):
    node = Node(state= problem.Result(parent.state,action),
                path_cost=parent.path_cost+problem.Step_cost(parent.state,action),
                parent=parent, 
                action=action)
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
    print("Cost = {}".format(cost))


def make_node(start):
    node = Node(start)
    return node

visit=[]
tmp=[]
def bestfs(problem,fringe):
    start_node=make_node(problem.start)
    fringe.append(start_node)    
    tmp.append(start_node.state)

    while fringe:
        print("fringe: ",end="")
        for i in fringe:
            print("({} {}+{}={})".format(i.state,i.h,i.path_cost,i.h+i.path_cost),end=" ")
        print()    

        node=fringe.pop(0)   
        tmp.remove(node.state)
        visit.append(node.state)    
        print(node.state,'*',sep='')
        if problem.goal_test(node.state):
            return Solution(node)
        
        for action in range(problem.Actions(node.state).__len__()):
            child = child_node(problem,node,action) 
            print(child.state)
            if child.state in visit:
                continue          
            fringe.append(child)
            fringe.sort()
            tmp.append(child.state)
        


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


hn={
    "Arab":366,
    "Bucharest":0,
    "Craiova":160,
    "Drobeta":242,
    "Eforie":141,
    "Fagaras":178,
    "Giurgiu":77,
    "Hirsova":151,
    "Iasi":226,
    "Lugoj":244,
    "Mehadia":241,
    "Neamt":234,
    "Oradea":380,
    "Pitesti":98,
    "Rimnicu Vilcea":193,
    "Sibiu":253,
    "Timisoara":329,
    "Urziceni":80,
    "Vaslui":199,
    "Zerind":374
}

start = "Arab"
end ="Bucharest"
fringe=[]
problem = Problem(graph,hn,start,end)
bestfs(problem,fringe)
