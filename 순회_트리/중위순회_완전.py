def lvr(n,k): #중위순회
    if(n<=k):
        lvr(n*2,k) # 왼쪽 자식으로 이동
        print(tree[n], end='')
        lvr(n*2+1,k) # 오른쪽 자식으로 이동

T = 10
for tc in range(1,T+1):
    N = int(input())
    tree = [0]*(N+1)
    for i in range(N):
        node = list(input().split())
        tree[int(node[0])] = node[1]

    print("#{}".format(tc), end=" ")
    lvr(1,N)
    print()

