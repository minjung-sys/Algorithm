from itertools import count
import sys

def solve(idx, res):
    global count
    if idx >= n:
        return
    
    res += k[idx]

    if res ==s:
        count += 1
    
    solve(idx+1,res)
    solve(idx+1,res - k[idx])

n, s = map(int, sys.stdin.readline().split())
k = list(map(int, sys.stdin.readline().split()))
count = 0 
solve( 0,0 )
print(count)

#재귀와 백트래킹 사용 
#현재의 index가 정수보다 크면 return 
#수열에 현재 index 정수를 더함
#현재 수열의 합이 s 라면 count
#현재 idx 정수를 더한 값을 백트래킹 함수에 넣어 재귀적으로 탐색
# 위 탐색이 끝난 후에 현재 index 정수를 더하지 않은 값을 재귀적으로 다시 탐색 