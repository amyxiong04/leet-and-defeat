class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for stone in stones:
            heapq.heappush(heap, -stone)


        while len(heap) > 1:
            x = -heap[0] # heaviest
            heapq.heappop(heap)

            y = -heap[0] # second heaviest
            heapq.heappop(heap)

            if x != y:
                heapq.heappush(heap, -(x - y))

        if len(heap):
            return -heap[0]
        return 0