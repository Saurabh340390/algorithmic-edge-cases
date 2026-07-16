class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        symbolMap = {}
        wordSet = set()
        def isMatch(sIndex, pIndex):
            if pIndex >= len(pattern):
                return sIndex == len(s)
            symbol = pattern[pIndex] 
            if symbol in symbolMap:
                word = symbolMap[symbol]
                if s[sIndex:(sIndex+len(word))] == word:
                    return isMatch(sIndex+len(word), pIndex+1)
                else:
                    return False
            for idx in range(sIndex, len(s)):
                newWord =  s[sIndex:idx+1] 
                if newWord in wordSet :
                    continue
                else:
                    wordSet.add(newWord)
                    symbolMap[symbol] = newWord
                    if isMatch(sIndex+len(newWord), pIndex+1) :
                        return True
                    else:
                        del symbolMap[symbol]
                        wordSet.remove(newWord)
            return False
        return isMatch(0,0)
