def lvr(n): #중위순회
    if(n>0):
        lvr(ch1[n]) # 왼쪽 자식으로 이동
        print(S[n], end='')
        lvr(ch2[n]) # 오른쪽 자식으로 이동

T = 10
for tc in range(1,T+1):
    N = int(input())
    ch1 = [0]*(N+1)
    ch2 = [0]*(N+1)
    S = [0]*(N+1)
    for i in range(N):
        node = list(input().split())
        if len(node) == 4 :
            ch1[int(node[0])] = int(node[2])
            ch2[int(node[0])] = int(node[3])
        elif len(node) == 3 :
            ch1[int(node[0])] = int(node[2])
        S[int(node[0])] = node[1]
    print("#{}".format(tc), end=" ")
    lvr(1)
    print()

