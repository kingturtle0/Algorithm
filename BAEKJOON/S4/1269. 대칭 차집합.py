N, M = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))
ans = A.union(B).difference(A.intersection(B))
print(len(ans))
