def word_break_print(s, dictionary):
    words = set(dictionary)
    memo = {}
    def solve(substring):
        if substring in memo: return memo[substring]
        if not substring: return [""]
        res = []
        for word in words:
            if substring.startswith(word):
                sub_res = solve(substring[len(word):])
                for item in sub_res:
                    res.append(word + (" " + item if item else ""))
        memo[substring] = res
        return res
    result = solve(s)
    return "Yes" if result else "No", result
d = ["i", "like", "sam", "sung", "samsung", "mobile", "ice", "cream", "icecream", "man", "go", "mango"]
print(word_break_print("ilike", d))
print(word_break_print("ilikesamsung", d))