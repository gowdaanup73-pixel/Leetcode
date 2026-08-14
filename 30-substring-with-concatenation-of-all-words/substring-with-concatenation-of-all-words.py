class Solution:
    def findSubstring(self, s, words):
        wordLen = len(words[0])
        numWords = len(words)
        totalLen = wordLen * numWords
        n = len(s)
        result = []
    
        if n < totalLen:
            return result
    
        needed = Counter(words)
        
        for offset in range(wordLen):
            left = offset
            count = 0
            window = Counter()
        
            for start in range(offset, n - wordLen + 1, wordLen):
                piece = s[start : start + wordLen]
            
                if piece in needed:
                    window[piece] += 1
                    count += 1
                    
                    while window[piece] > needed[piece]:
                        leftWord = s[left : left + wordLen]
                        window[leftWord] -= 1
                        count -= 1
                        left += wordLen
                    
                    if count == numWords:
                        result.append(left)
                        leftWord = s[left : left + wordLen]
                        window[leftWord] -= 1
                        count -= 1
                        left += wordLen
                else:
                    window.clear()
                    count = 0
                    left = start + wordLen
    
        return result