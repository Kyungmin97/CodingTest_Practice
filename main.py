
#DFS Part
#1
"""
def dfs(graph, v, visited):
    visited[v]=True
    #방문처리
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            #재귀 호출

graph=[
    [],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]
]

visited=[False]*9
dfs(graph,1,visited)
"""

#BFS Part
#2
"""
from collections import deque
def bfs(graph, start, visited):
    queue=deque([start])
    visited[start]=True
    #방문처리
    while queue:
        v=queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
                #재귀 호출


graph=[
    [],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]
]

visited=[False]*9
bfs(graph,1,visited)

"""
#3
"""

n,m=map(int,input().split())

graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):
    if x>=n or x<0 or y<0 or y>=m:
        return False
    if graph[x][y]==1:
        return False

    graph[x][y]=1
    dfs(x+1,y)
    dfs(x-1,y)
    dfs(x,y+1)
    dfs(x,y-1)
    return True

result=0
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            result+=1
print(result)
"""
#4 1260

"""
from collections import deque

n,m,v=map(int,input().split())

graph=[]

for i in range(m):
    graph.append(list(map(int,input().split())))

def dfs(graph,v,visited):
    print(v, end=' ')
    visited[v]=True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

def bfs(graph, start, visited):
    queue=deque([start])
    visited[start]=True
    #방문처리
    while queue:
        v=queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
                #재귀 호출



visited=[False] * (n+1)

for _ in range(m):
    graph[a].append(b)


for i in range(1,n+1):
    graph[i].sort()

dfs(v)
visited=[False] * (n+1)
print()
bfs(v)
"""

#5 2178
"""
from collections import deque

n,m=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input())))
dx=[-1,1,0,0]
dy=[0,0,-1,1]


def bfs(x,y):
    queue=deque()
    queue.append((x,y))

    while queue:
        x,y=queue.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))

    return graph[n-1][m-1]
print(bfs(0,0))
"""

#6 2667
"""
from collections import deque
dy=[0,0,-1,1]
dx=[-1,1,0,0]

def bfs(graph,a,b):
    n=len(graph)
    queue=deque()
    queue.append((a,b))
    graph[a][b]=0
    count=1

    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx,ny))
                count += 1
    return count

n=int(input())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

cnt=[]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt.append(bfs(graph,i,j))

cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])
"""

#7 2606 DFS
"""
n=int(input())
m=int(input())
graph=[[]*n for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
visited=[0] * (n+1)
def dfs(start):
    global cnt
    visited[start] = 1
    for i in graph[start]:
        if visited[i]==0:
            dfs(i)
            cnt += 1

dfs(1)
print(cnt)
"""

#8 1012
"""
from collections import deque

dx=[0,0,1,-1]
dy=[1,-1,0,0]

t=int(input())

def bfs(graph,a,b):
    queue = deque()
    queue.append((a,b))
    graph[a][b] = 0

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx,ny))
    return

for i in range(t):
    cnt = 0
    n,m,k=map(int,input().split())
    graph = [[0]*m for _ in range(n)]

    for j in range(k):
        x,y = map(int,input().split())
        graph[x][y]=1

    for a in range(n):
        for b in range(m):
            if graph[a][b] == 1:
                bfs(graph,a,b)
                cnt += 1
    print(cnt)
"""

#9 7576
"""
from collections import deque

m,n=map(int,input().split())
graph=[]
queue = deque([])
for i in range(n):
    graph.append(list(map(int,input().split())))

    for j in range(m):
        if graph[i][j]==1:
            queue.append([i,j])

dx, dy = [-1,1,0,0], [0,0,-1,1]

def bfs():
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx, ny = dx[i]+x, dy[i]+ y
            if n>nx>=0 and m>ny>=0 and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx,ny])

bfs()
res=0
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))
print(graph)
print(res-1)
"""

#10 1697

print(1)























