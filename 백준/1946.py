import sys

T = int(input())

for i in range(0,T):
    count=1
    people = []

    N = int(input())
    for i in range(N):
        pap, inter = map(int,sys.stdin.readline().split())
        people.append([pap,inter])

    people.sort()#서류기준으로 오름차순 정렬
    max = people[0][1]
    for i in range(1,N):
        if max >people[i][1]:
            count+=1
            max = people[i][1]

    print(count)