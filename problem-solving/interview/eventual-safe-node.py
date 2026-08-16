# from leetcode
# 802. Find Eventual Safe States
# https://leetcode.com/problems/find-eventual-safe-states/description/


def eventualSafeNodes(self, graph):
    import collections
    safe = [False] * N

    graph = list(map(set, graph))
    rgraph = [set() for _ in range(N)]
    q = collections.deque()

    for i, js in enumerate(graph):
        if not js:
            q.append(i)
        for j in js:
            rgraph[j].add(i)

    while q:
        j = q.popleft()
        safe[j] = True
        for i in rgraph[j]:
            graph[i].remove(j)
            if len(graph[i]) == 0:
                q.append(i)

    return [i for i, v in enumerate(safe) if v]


if __name__ == '__main__':
    results = eventualSafeNodes(0, [[1, 2], [2, 3], [5], [0], [5], [], []])
    print(results)