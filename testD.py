from queue import PriorityQueue

q = PriorityQueue()

# hn={
#     "Arab":366,
#     "Bucharest":0,
#     "Craiova":160,
#     "Dobreta":242,
#     "Eforie":141,
#     "Fagaras":178,
#     "Giurgiu":77,
#     "Hirsova":151,
#     "Iasi":226,
#     "Lugoj":244,
#     "Mehadia":241,
#     "Neamt":234,
#     "Oradea":380,
#     "Pitesti":98,
#     "Rimnicu Vilcea":193,
#     "Sibiu":253,
#     "Timisoara":329,
#     "Urziceni":80,
#     "Vaslui":199,
#     "Zerind":374
# }

# q.put((hn["Zerind"],"Z"))
# q.put((hn["Sibiu"],"S"))
# q.put((hn["Timisoara"],"T"))
# q.get_nowait()
# while not q.empty():
#     item = q.get()
#     print(item[1])

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
print(graph["Arab"][0][1])