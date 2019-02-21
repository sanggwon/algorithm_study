def f(n):
    if (n>=2 and memo[n] == 0) :
        memo[n] = f(n-1)+f(n-2)
    return memo[n]

N = 10
memo = [0]*(N+1)
memo[0] = 0
memo[1] = 1

print(f(N))

F = [0]*(N+1)
F[0] = 0
F[1] = 1
for n in range(2,N+1):
    F[n] = F[n-1] + F[n-2]
print(F)