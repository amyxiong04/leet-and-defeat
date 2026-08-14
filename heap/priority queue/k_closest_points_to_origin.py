class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [] # max heap storing k closest points to the origin 
        ans = []

        for point in points:
            x = point[0]
            y = point[1]

            distance = x**2 + y**2
            
            heapq.heappush(heap, [-distance, point])
            
            if len(heap) > k:
                heapq.heappop(heap)

        for distance, point in heap:
            ans.append(point)

        return ans

        