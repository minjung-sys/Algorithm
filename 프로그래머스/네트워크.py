def bfs(n,computers,com,visited):
    visited[com] = True
    queue = []
    queue.append(com)
    while queue:
        com = queue.pop(0)
        visited[com] = True
        for connect in range(n):
            if connect != com and computers[com][connect] == 1:
                if visited[connect] == False:
                    queue.append(connect)
def solution(n,computers):
    answer = 0
    visited = [False for i in range(n)]
    for com in range(n):
        if visited[com] is False:
            bfs(n,computers,com,visited)
            answer+=1
    return answer

