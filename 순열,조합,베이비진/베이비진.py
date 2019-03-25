def npr(n,k): #n이 순열의 길이, k는 숫자를 결정할 자리
    if n==k:
        # 앞의 반이 run or triplet
        r,t=0,0
        if(p[0]+1==p[1] and p[1]+1==p[2]): #run
            r=1
        if(p[0]==p[1]==p[2]):
            t=1
        #뒤의 반이 run or triplet
        if (p[3]+1 ==p[4] and p[4] +1 == p[5]): #run
            r += 1
        if(p[3]==p[4]==p[5]):
            t+=1
        if r+t ==2:
            return 1
    else:
        for i in range(k,n):
            p[i],p[k] = p[k], p[i]
            if npr(n,k+1)==1:
                return 1 # 베이비 진이라면 계속 1리턴
            p[i], p[k] = p[k], p[i]
        return 0
p = [2, 2, 6, 7, 8,2]
npr(6,0)