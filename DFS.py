# nodes = input("Enter the number of Nodes:")
# nodes = int(nodes)
# for i in range(0,nodes):
#     print(i)

matrix = [
    [0,1,1,1,1],
    [1,0,0,0,0],
    [1,0,0,0,0],
    [1,0,0,0,0],
    [1,0,0,0,0]   
    ]

# print(matrix[2][1])

visited = [ False, False, False, False, False ]

def DFS(a: int):
   
    print(a)
    visited[a] = True
    for j in range(5):
        if matrix[a][j] == 1 and visited[j] == False:
            DFS(j)
   

DFS(2)