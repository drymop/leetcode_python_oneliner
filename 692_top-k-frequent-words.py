class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return (lambda C:sorted(set(words),key=lambda w:(-C[w],w))[:k])(Counter(words))
