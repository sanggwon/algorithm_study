import sys
from itertools import permutations

def find():
    min  = 100
    for p in permutations(range(N)):        # 순열 생성
        s = 0
        for i in range(N):
            s += m[i][p[i]]                 # 순열을 이용해 합 구하기
        if min > s:
            min = s;
    return min

sys.stdin = open('input.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    m = [list(map(int,input().split())) for x in range (N)] # 중첩리스트에 숫자 저장
    print('#{} {}'.format(tc, find()))
    

  
