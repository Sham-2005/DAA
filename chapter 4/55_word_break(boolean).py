def word_break(s, wordDict):
    dp = [False] * (len(s) + 1)
    dp[0] = True
    words = set(wordDict)
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in words:
                dp[i] = True
                break
    return dp[-1]
print(word_break("leetcode", ["leet", "code"]))      
print(word_break("applepenapple", ["apple", "pen"])) 
print(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"])) 