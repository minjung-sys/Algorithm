#폴로이드 와샬 알고리즘 
MAX =10000

N=int(input())
inputMap=[[0 for col in range(N)] for row in range(N)]
for i in range(0,N) :
    for j,m in enumerate(map(int,input().split())) :
        inputMap[i][j] = m

for k in range(0,N) :
    for i in range(0,N):
        for j in range(0,N):
            if inputMap[i][k] and inputMap[k][j] :
                inputMap[i][j] = 1

for i in range(0,N):
    str_result = ""
    for j in range(0,N):
        str_result+= str(inputMap[i][j])+" "
    print(str_result)

