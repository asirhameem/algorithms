import queue as que;

queue = que.Queue();

graph = {
    "Arad": {"Timisoara": 118, "Sibiu": 140,"Zerind": 75},
    "Zerind": {"Arad": 75, "Oradea": 71},
    "Oradea": {"Zerind": 71, "Sibiu": 151},
    "Timisoara": {"Arad": 118, "Lugoj": 111},
    "Lugoj": {"Timisoara": 111, "Mehadia":70},
    "Mehadia": {"Lugoj": 70, "Dobreta": 75},
    "Dobreta": {"Mehadia":75, "Craiova":120},
    "Craiova": {"Dobreta": 120, "RimnicuVilcea": 146, "Pitesi": 138},
    "RimnicuVilcea": {"Craiova": 146, "Pitesi": 97, "Sibiu":80},
    "Sibiu": {"Arad": 140, "Oradea":151, "RimnicuVilcea": 80, "Fagaras": 99},
    "Fagaras": {"Sibiu": 99, "Bucharest":211},
    "Pitesi": {"Bucharest": 101, "RimnicuVilcea": 97, "Craiova": 138},
    "Bucharest": {"Pitesi": 101, "Fagaras": 211, "Giurgiu": 90, "Urziceni": 85},
    "Giurgiu": {"Bucharest": 90},
    "Urziceni": {"Bucharest": 85, "Hirsova": 98, "Vaslui": 142},
    "Hirsova": {"Urziceni": 98, "Eforie": 86},
    "Eforie": {"Hirsova": 86},
    "Vaslui": {"Urziceni": 142, "Iasi": 92},
    "Iasi": {"Vaslui": 92, "Neamt": 87},
    "Neamt": {"Iasi": 87}
};

goal = "Bucharest";
flag = 0;

visited = {
    "Arad": 0,
    "Zerind": 0,
    "Oradea": 0,
    "Timisoara": 0,
    "Lugoj": 0,
    "Mehadia": 0,
    "Dobreta": 0,
    "Craiova": 0,
    "RimnicuVilcea": 0,
    "Sibiu": 0,
    "Fagaras": 0,
    "Pitesi": 0,
    "Bucharest": 0,
    "Giurgiu": 0,
    "Urziceni": 0,
    "Hirsova": 0,
    "Eforie": 0,
    "Vaslui": 0,
    "Iasi": 0,
    "Neamt": 0
};

parent = {
    "Arad": None,
    "Zerind": None,
    "Oradea": None,
    "Timisoara": None,
    "Lugoj": None,
    "Mehadia": None,
    "Dobreta": None,
    "Craiova": None,
    "RimnicuVilcea": None,
    "Sibiu": None,
    "Fagaras": None,
    "Pitesi": None,
    "Bucharest": None,
    "Giurgiu": None,
    "Urziceni": None,
    "Hirsova": None,
    "Eforie": None,
    "Vaslui": None,
    "Iasi": None,
    "Neamt": None
};

queue.put("Arad");

while queue.empty() is False:
    frontier = queue.get();
    visited[frontier] = 2;
    for x in graph[frontier]:
        if(visited[x] != 1 and visited[x] != 2):
            parent[x] = frontier;
            if(x == goal):
                print("Goal Found!");
                flag = 1;
                break;
            else:
                queue.put(x);
                visited[x] = 1;
    if( flag == 1):
        while parent[x] != None:
            print(x);
            x = parent[x];
        print(x);
        break;

