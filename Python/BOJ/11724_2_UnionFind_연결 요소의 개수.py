from sys import stdin


def find(x):
    if x == root[x]:
        return x
    root[x] = find(root[x])
    return root[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return False

    if rank[x] < rank[y]:
        root[x] = y
    else:
        root[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1
    return True


input = stdin.readline
V, E = map(int, input().split())
rank = [1] * (V + 1)
root = [i for i in range(V + 1)]
for edge in range(E):
    u, v = map(int, input().split())
    union(u, v)

res = set()
for v in range(1, V + 1):
    res.add(find(v))

print(len(res))
