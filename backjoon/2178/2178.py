import sys
from collections import deque
sys.stdin = open('2178.txt')
# sys.setrecursionlimit(99999)


# def dfs(y, x, cnt):
#     global result
#     if y == N-1 and x == M-1:
#         # print(cnt)
#         result.append(cnt)
#     else:
#         for i in range(4):
#             dy = y + Y[i]
#             dx = x + X[i]
#             # 해당 범위 벗어나거나 갈 수 있는 길이 아니면 pass
#             if dx < 0 or dx > M-1 or dy < 0 or dy > N-1 or maze[dy][dx] == 0:
#                 pass
#             else:
#                 # 방문했던 곳이면 제꾸고
#                 if visited[dy][dx] == 1:
#                     pass
#                 else:
#                     # 방문안했으면 방문 표시
#                     visited[dy][dx] = 1
#                     dfs(dy, dx, cnt+1)
#                     # 나뉘어지는 지점부터 다시 시작해야하니까 미방문 처리
#                     visited[dy][dx] = 0
def bfs(y, x):
    queue = deque()
    queue.append((y, x))
    while queue:
        y, x = queue.popleft()
        # if y == N-1 and x == M-1:
        #     result.append(cnt)
        #     return result
        for i in range(4):
            dy = y + Y[i]
            dx = x + X[i]
            if dy < 0 or dx < 0 or dy > N-1 or dx > M-1 or maze[dy][dx] == 0:
                pass
            else:
                if maze[dy][dx] == 1:
                    queue.append((dy, dx))
                    visited[dy][dx] += maze[dy][dx]


N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
# arr = [[0] * (M+1) for _ in range(N+1)]
graph = []
# for i in range(N):
#     graph.append(list(map(int, input())))
# print(graph)
visited = [[0 for _ in range(M)] for _ in range(N)]
# visited = [0] *(n+1)

# print(maze)
# print(visited)
result = []
cnt = 0
#상하좌우
Y = [-1, 1, 0, 0]
X = [0, 0, -1, 1]

# for i in range(N):
#     for j in range(M):
#         # print(i, j)
#         visited[i][j] = maze[i][j]
#시작지점도 셈해줘야하니까 cnt 1 부터 시작
# dfs(0, 0, 1)
print(bfs(0, 0))
# print(min(result))
# print(result)