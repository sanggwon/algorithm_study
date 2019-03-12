def bfs(n, m):
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    done = 0
    rare = 0 # 안익은 토마토 수
    cnt = 0 # 1일이후 익은 토마토 수

    q = [0]*n*m*2
    front = -1
    rear = -1
    visited = [[0]*m for i in range(n)]
    for i in range(N):
        for j in range(M):
            if (box[i][j] == 0):
                rare +=1
            elif (box[i][j] == 1):
                rear += 1
                q[rear] = i
                rear += 1
                q[rear] = j
                visited[i][j] = 1
                done += 1
    if(rare == 0 and done != 0):
        return 0
    last = 0
    while(front != rear):
        front += 1
        i = q[front]
        front += 1
        j = q[front]
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if(ni>=0 and ni<n and nj>=0 and nj<m):
                if(box[ni][nj] == 0 and visited[ni][nj] == 0):
                    rear += 1
                    q[rear] = ni
                    rear += 1
                    q[rear] = nj
                    visited[ni][nj] = visited[i][j] + 1
                    last = visited[ni][nj]
                    cnt += 1
    if (cnt != rare): # 안익고 남은 토마토가 있으면
        return -1
    else:
        return last -1

M, N = map(int, input().split())
box = [list(map(int, input().split())) for i in range(N)]
print(bfs(N, M))