class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        counts = Counter(tasks)

        max_freq = max(counts.values())
        max_count = 0
        for c in counts.values():
            if c == max_freq:
                max_count += 1
        frame_len = (max_freq - 1) * (n + 1) + max_count
        return max(frame_len, len(tasks))
