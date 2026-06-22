import heapq

def kClosest(points, k):
    heap = []

    for x, y in points:
        dist = x * x + y * y
        heapq.heappush(heap, (dist, [x, y]))

    ans = []

    for _ in range(k):
        ans.append(heapq.heappop(heap)[1])

    return ans