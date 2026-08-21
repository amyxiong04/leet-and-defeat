class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        intervals = 0

        for task in tasks:
            freq[task] = freq.get(task, 0) + 1

        max_freq = max(freq.values())
        max_count = 0

        for task in freq:
            if freq[task] == max_freq:
                max_count += 1

        intervals = ((max_freq - 1) * n) + max_freq + max_count - 1

        return max(intervals, len(tasks))

        
        