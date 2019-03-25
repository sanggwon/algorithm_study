def npr(n,k): #n이 순열의 길이, k는 숫자를 결정할 자리
    if n==k:
        print(p)
    else:
        for i in range(k,n):
            p[i],p[k] = p[k], p[i]
            npr(n,k+1)
            p[i], p[k] = p[k], p[i]
p = [1, 2, 3, 4, 5]
npr(5,0)