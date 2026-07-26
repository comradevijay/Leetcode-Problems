class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = defaultdict(int)
        for word in words:
            freq[word] += 1

        bucket = [[] for _ in range(len(words) + 1)]

        for word, count in freq.items():
            bucket[count].append(word)

        ans = []

        for i in range(len(words), 0, -1):
            if not bucket[i]:
                continue
            bucket[i].sort()

            for word in bucket[i]:
                ans.append(word)
                if len(ans) == k:
                    return ans

        return ans