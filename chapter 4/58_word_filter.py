class WordFilter:
    def __init__(self, words):
        self.d = {}
        for idx, word in enumerate(words):
            l = len(word)
            for i in range(l + 1):
                for j in range(l + 1):
                    self.d[word[:i] + "#" + word[l-j:]] = idx
    def f(self, pref, suff):
        return self.d.get(pref + "#" + suff, -1)
wf = WordFilter(["apple"])
print(f"Index: {wf.f('a', 'e')}") 