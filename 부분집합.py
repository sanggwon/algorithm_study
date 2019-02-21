# for i in range(2**N):
#     #i를 비트 단위로 접근 
#     for j in range(N):
#         if(i&(1<<j) !=0): #A[j]가 포함되면
#             print(A[j], end="")
T = 5
A = [-7,-3,-2,5,8]
my_sum = 0
result = 1
for i in range(2**T):
    for j in range(T):
        if(i&(1<<j) !=0):
            my_sum += A[j]
            result *= my_sum
    my_sum = 0
if result == 0:
    print("True")
else :
    print("False")
        
